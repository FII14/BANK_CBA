import json
import os
from datetime import datetime
from colorama import Fore

b = Fore.LIGHTBLUE_EX
r = Fore.RESET
h = Fore.LIGHTGREEN_EX
m = Fore.LIGHTRED_EX
p = Fore.LIGHTWHITE_EX

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_pin():
    pin = input(f"{p}Buat PIN baru: ")
    with open('pin.json', 'w') as file:
        json.dump({'pin': pin}, file)
        clear_srceen()

def reset_pin():
    pin = input(f"{p}Masukkan PIN baru: ")
    with open('pin.json', 'w') as file:
        json.dump({'pin': pin}, file)
        clear_screen()

def check_pin():
    if not os.path.isfile('pin.json'):
        create_pin()
        return True

    with open('pin.json', 'r') as file:
        data = json.load(file)
        pin = data['pin']

    while True:
        input_pin = input(f"{p}Masukkan PIN: ")
        if input_pin == pin:
            clear_screen()
            return True
        elif input_pin == '0':
            reset_pin()
            return True
        else:
            print(f"{m}[-] {p}PIN salah. Silakan coba lagi.{r}")


while True:
    if check_pin():
        while True:
            now = datetime.now()
            print(f"""{b}
 ____    _    _   _ _  __   ____ ____    _
| __ )  / \  | \ | | |/ /  / ___| __ )  / \
|  _ \ / _ \ |  \| | ' /  | |   |  _ \ / _ \
| |_) / ___ \| |\  | . \  | |___| |_) / ___ \
|____/_/   \_\_| \_|_|\_\  \____|____|_/   \_|{r}

Tanggal: {now.strftime("%d/%m/%Y")}
Jam: {now.strftime("%H:%M:%S")}\n
[1]. Simpan uang
[2]. Ambil uang
[3]. Muat uang
[4]. Keluar
{r}""")
            pilihan = input("\nPilih opsi (1/2/3/4): ")

            if pilihan == '1':
                jumlah_uang = float(input("Masukkan jumlah uang yang ingin disimpan: "))
                try:
                    with open('data_saldo.json', 'r') as file:
                        data = json.load(file)
                except FileNotFoundError:
                    data = {'saldo_rp': 0}

                data['saldo_rp'] += jumlah_uang

                with open('data_saldo.json', 'w') as file:
                    json.dump(data, file)

                clear_screen()
                print(f"\n{h}[+] {p}Berhasil menyimpan uang sebesar RP.{int(jumlah_uang)}{r}")

            elif pilihan == '2':
                jumlah_uang = float(input("Masukkan jumlah uang yang ingin diambil: "))
                try:
                    with open('data_saldo.json', 'r') as file:
                        data = json.load(file)
                except FileNotFoundError:
                    print(f"{m}[-] {p}Data saldo tidak ditemukan.{r}")
                    continue

                if jumlah_uang <= data['saldo_rp']:
                    data['saldo_rp'] -= jumlah_uang

                    with open('data_saldo.json', 'w') as file:
                        json.dump(data, file)

                    clear_screen()
                    print(f"{h}[+] {p}Berhasil mengambil uang sebesar RP.{int(jumlah_uang)}{r}\n")
                else:
                    clear_screen()
                    print(f"\n{m}[-] {p}Saldo tidak mencukupi.{r}")

            elif pilihan == '3':
                try:
                    with open('data_saldo.json', 'r') as file:
                        data = json.load(file)
                        saldo_rp = data['saldo_rp']
                        clear_screen()
                        print(f"\n{h}[+] {p}Saldo Anda saat ini adalah RP.{int(saldo_rp)}{r}")
                except FileNotFoundError:
                    print(f"{m}[-] {p}Data saldo tidak ditemukan.{r}")

            elif pilihan == '4':
                break

            else:
                print(f"{m}[-] {p}Pilihan tidak valid. Silakan coba lagi.{r}")
        break
