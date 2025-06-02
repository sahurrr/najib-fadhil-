def main():
    # Inisialisasi daftar film kosong
    movie_list = ["Jumbo", "Najib is hero", "Tung Tung Sahur"]

    while True:
        print("\n=== Aplikasi Manajemen Daftar Film ===")
        print("1. Tambah Film")
        print("2. Hapus Film")
        print("3. Lihat Semua Film")
        print("4. Cari Film")
        print("5. Total Film")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        # 1. Tambah Film (append())
        if pilihan == "1":
            film = input("Masukkan judul film: ").strip()
            if film:
                movie_list.append(film)
                print(f"Film '{film}' berhasil ditambahkan!")
            else:
                print("Judul film tidak boleh kosong!")

        # 2. Hapus Film (remove())
        elif pilihan == "2":
            if not movie_list:
                print("Daftar film kosong!")
                continue

            print("Daftar Film:", movie_list)
            film = input("Masukkan judul film yang ingin dihapus: ").strip()
            if film in movie_list:
                movie_list.remove(film)
                print(f"Film '{film}' dihapus dari daftar!")
            else:
                print(f"Film '{film}' tidak ditemukan.")

        # 3. Lihat Semua Film (iterasi list)
        elif pilihan == "3":
            if not movie_list:
                print("Daftar film kosong!")
            else:
                print("\n=== Daftar Film ===")
                for idx, film in enumerate(movie_list, start=1):
                    print(f"{idx}. {film}")

        # 4. Cari Film (in operator)
        elif pilihan == "4":
            film = input("Cari judul film: ").strip()
            if film in movie_list:GR
                print(f"Film '{film}' ada dalam daftar!")
            else:
                print(f"Film '{film}' tidak ditemukan.")

        # 5. Total Film (len())
        elif pilihan == "5":
            print(f"Total film dalam daftar: {len(movie_list)}")

        # 6. Keluar
        elif pilihan == "6":
            print("Terima kasih! Sampai jumpa.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih 1-6.")

if __name__ == "__main__":
    main()