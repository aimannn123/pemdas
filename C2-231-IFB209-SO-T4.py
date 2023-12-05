#import library yang digunakan
import time
import datetime

#array files untuk directory
files = [".", "..", "Desktop", "Documents", "Downloads", "Music", "Pictures", "Video"]
#inisialisasi variabel boolean yang masuk dan menyetelnya ke False sebagai tanda untuk menunjukkan apakah pengguna masuk ke suatu sistem atau tidak.
loggedin = False

#fungsi print_slow, mengambil parameter teks (mungkin string) dan mencetaknya karakter dengan efek proses lambat
def print_slow(text):
    #iterasi melalui setiap char dalam string text
    for char in text:
        #blok kode yang diulang, mencetak karakter char ke konsol.
        print(char, end='', flush=True)
        # inner loop (for _ in range(4000000):) introduces the delay.
        for _ in range(4000000):
            pass

#definisi fungsi bernama simulasi_progress() yang mengambil dua parameter yaitu process_name dan duration
def simulate_progress(process_name, duration):
    #for loop diulang 100 kali, menyimulasikan penyelesaian proses dalam 100 kelipatan 1%.
    for i in range(1, 101):
        #menghitung persentase progress saat ini dengan menetapkan nilai i ke variabel progress
        progress = i
        #delay dihitung dengan membagi total durasi (duration) dengan jumlah peningkatan progress (100)
        time.sleep(duration / 100)  # Simulating a process in progress
        #mencetak informasi progress terkini ke konsol
        # end untuk mencegah kursor berpindah ke baris berikutnya
        # flush=true untuk segera memaksa output ke konsol.
        print(f"\r{process_name}... {progress}%  ", end='', flush=True)

def check_hardware():
    print_slow("\nMengecek Hardware...                ")

    # Pengecekan RAM
    ram_slots = 4
    ram_per_slot = [16, 16, 0, 0]  # Jumlah RAM di setiap slot
    total_ram = sum(ram_per_slot)

    print_slow(f"\n    Mengecek slot RAM:")
    for slot_number, size in enumerate(ram_per_slot, start=1):
        if size > 0:
            print_slow(f"\n        Slot {slot_number}:(Tersedia) {size}GB DDR5 4800MHz")
        else:
            print_slow(f"\n        Slot {slot_number}:(Kosong)")

    print_slow(f"\n       Total RAM: {total_ram}GB")

    # Pengecekan M.2 Slot
    m2_slot_size = 1  # Ukuran M.2 slot dalam TB
    print_slow(f"\n\n    Mengecek M.2 Slot:   \n        M.2 Slot:(Tersedia) {m2_slot_size}TB")

    # Pengecekan Slot SATA
    sata_slot_count = 2  # Jumlah slot SATA
    print_slow(f"\n\n    Mengecek Slot SATA:")
    for slot_number in range(1, sata_slot_count + 1):
        print_slow(f"\n        Slot SATA {slot_number}:(Kosong)")

    # Pengecekan Slot Ekspansi
    print_slow("\n\n    Mengecek Slot Ekspansi:   \n        Slot Ekspansi: (Tersedia) Terhubung dengan VGA")

    # Pengecekan DisplayPort
    print_slow("\n\n    Mengecek Displayport:   \n        Displayport: (Tersedia) Terhubung dengan Monitor")

    # Pengecekan USB 2.0
    usb_2_count = 2
    usb_2_status = ["Terhubung dengan Mouse", "Terhubung dengan Keyboard"]
    print_slow(f"\n\n    Mengecek USB 2.0 Ports:")
    for port_number, status in zip(range(1, usb_2_count + 1), usb_2_status):
        print_slow(f"\n        USB 2.0 Port {port_number}: (Tersedia) {status}")

    # Pengecekan USB Type-C
    print_slow("\n\n    Mengecek USB Type-C:   \n        USB Type-C: (Kosong)")

    # Pengecekan Port Audio Jack
    audio_jack_count = 3
    audio_jack_status = ["Terhubung dengan Speaker", "kosong", "kosong"]
    print_slow(f"\n\n    Mengecek Port Audio Jack:")
    for port_number, status in zip(range(1, audio_jack_count + 1), audio_jack_status):
        print_slow(f"\n        Audio Jack {port_number}: ({status})")

    print('\nPOST complete!')

#fungsi boot
def boot():
    # Simulasikan proses boot dengan progress bar dan durasi 5 detik
    simulate_progress("Memulai proses boot", 5)
    # Cetak 'Siap!' setelah Memulai proses boot
    print('Ready!')

    # Simulasikan proses POST dengan progress bar dan durasi 3 detik
    simulate_progress("Memulai proses Power-on self-test (POST)", 3)
    # Cetak 'Siap!' setelah memulai proses POST
    print('Ready!')

    # Simulasikan inisialisasi komponen perangkat keras dengan progress bar dan durasi 4 detik
    simulate_progress("Initializing hardware", 4)
    # Panggil fungsi check_hardware() untuk melakukan pemeriksaan perangkat keras
    check_hardware()  # Panggil fungsi check_hardware()

    # Simulasikan loading bootloader dengan progress bar dan durasi 2 detik
    simulate_progress("Loading bootloader", 2)
    # Cetak 'Siap!' setelah loading bootloader
    print('Ready!')

    # Simulasikan verifikasi integritas bootloader dengan progress bar dan durasi 2 detik
    simulate_progress("Verifying bootloader integrity", 2)
    # Cetak 'Siap!' setelah integritas bootloader diverifikasi
    print('Ready!')

    # Simulasikan proses booting kernel dengan progres bar dan durasi 3 detik
    simulate_progress("Booting kernel", 3)
    # Cetak 'Siap!' setelah kernel di-boot
    print('Ready!')

#fungsi login user
def login():
    #variabel yang dapat diakses dari mana saja dalam program
    global loggedin
    #menginisialisasi variabel attempts ke nilai 0, menyimpan jumlah upaya login pengguna
    attempts = 0

    #perulangan jumlah upaya login memasukkan username dan password dengan percobaan 3 kali
    while attempts < 3:
        username = input('Masukkan Username: ')
        password = input('Masukkan Password: ')

        # looping login
        # jika username=='admin' dan password =='1234'
        if username == 'admin' and password == '1234':
            #output
            print('Login Berhasil! Menunggu perintah selanjutnya')
            #inisialisasi variabel loggedin ke nilai True
            loggedin = True
            break
        #jika username!='admin' dan password !='1234'
        else:
            #ouput
            print('Login Gagal, Harap coba lagi!')
            #meningkatkan nilai variabel attempts sebesar 1
            attempts += 1
    #jika percobaan sudah 3 kali
    if attempts == 3:
        #output
        print('Login gagal mencoba 3 kali. Exiting Program')
        #keluar dari program
        exit()

    # Tampilkan pesan copyright
    print("Copyright (c) Corporation. All rights reserved.")
    time.sleep(1)

#program simulasi proses shell
#fungsi command dengan parameter user_input
def command(user_input):
    global files
    try:
        #perintah dir
        if user_input.lower() == 'dir':
            # perintah dir
            print("Directory of C:\\Users\\admin")
            for item in files:
                # Display the last modification time
                current_utc_time = datetime.datetime.utcnow()
                str_date_time = current_utc_time.strftime("%m/%d/%y, %H.%M")
                print(f"{str_date_time} <DIR> {item}")

        #jika user input mkdir
        elif user_input.lower().startswith('mkdir '):
            # perintah mkdir
            _, dirname = user_input.split(' ', 1)
            if dirname not in files:
                files.append(dirname)
                print(f"Direktori {dirname} berhasil dibuat.")
            else:
                print(f"Direktori sudah tersedia: {dirname}")

        #jika user input delete
        elif user_input.lower().startswith('delete '):
            # perintah delete
            _, filename = user_input.split(' ', 1)
            if filename in files:
                files.remove(filename)
                print(f"{filename} Berhasil dihapus.")
            else:
                print(f"File tidak ditemukan: {filename}")

        #jika user input pilih rename
        elif user_input.lower().startswith('rename '):
            # perintah rename
            _, old_name, new_name = user_input.split(' ', 2)
            if old_name in files:
                files[files.index(old_name)] = new_name
                print(f"File/Direktori {old_name} berhasil diubah menjadi {new_name}.")
            else:
                print(f"File/Direktori tidak ditemukan: {old_name}")

        #jika user input pilih date
        elif user_input.lower().startswith('date'):
            #perintah date
            print(f"The current date is:", datetime.datetime.now().strftime("%A %Y-%m-%d"))

        #jika user input pilih time
        elif user_input.lower().startswith('time'):
            #perintah time
            current_local_time = datetime.datetime.now()
            str_date_time = current_local_time.strftime("%H:%M:%S")
            print(f"The current time is: {str_date_time}")

        #jika user input pilih cls
        elif user_input.lower().startswith('cls'):
            # perintah cls
            print('\n' * 50)

        #jika user input pilih help
        elif user_input.lower() == 'help':
            #output
            print("For more information on a specific command, type help command-name")
            # perintah help
            print('CLS            Untuk membersihkan layar.')
            print('DIR            Untuk memperlihatkan file direktori.')
            print('MKDIR          Untuk membuat direktori.')
            print('DELETE         Untuk menghapus file.')
            print('RENAME         Untuk mengubah nama file')
            print('DATE           Untuk menampilkan tanggal direktori.')
            print('TIME           Untuk menampilkan waktu direktori.')
            print('HELP           Untuk memperlihatkan beberapa perintah.')
            print('SHUTDOWN       Untuk keluar dari sistem.')
        #jika kondisi diatas tidak memenuhi
        else:
            #hasil output
            print("Perintah tidak dikenal. Ketik 'help' untuk melihat perintah yang tersedia")
    except Exception as e:
        print(f"Error: {e}")

#Fungsi untuk melakukan booting sistem
boot()


# Utama saat login
#jika tidak login
while not loggedin:
    #user input
    user_input = input("Command> ")
    #jika input login
    if user_input == 'login':
        login()
        if loggedin:
            continue
    #jika tidak login
    else:
        #output kalimat agar user login
        print('Harap Login terlebih dahulu!')

#jika sudah login, perulangan while
while True:
    #input dari user
    user_input = input("C:\\Users\\admin> ")
    #jika user input pilih shutdown
    if user_input.lower() == 'shutdown':
        #output
        print('Shutting down the system')
        break

    if not loggedin:
        print('Harap Login terlebih dahulu!')
        continue
    #memanggil fungsi 'perintah' dengan input user
    command(user_input)