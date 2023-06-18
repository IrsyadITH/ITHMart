import os 

class PerpustakaanITH:
    def __init__(self):
        self.buku = {}
        self.buku_dibaca = {}

    def tambah_buku(self, nama_buku, penulis, penerbit, tahun_terbit, jenis_buku, ketersediaan, letak_buku):
        if nama_buku in self.buku:
            print("Buku sudah ada dalam sistem.")
        else:
            self.buku[nama_buku] = {
                'Penulis': penulis,
                'Penerbit': penerbit,
                'Tahun Terbit': tahun_terbit,
                'Jenis Buku': jenis_buku,
                'Ketersediaan': ketersediaan,
                'Letak Buku': letak_buku,
                'Dibaca': False
            }
            print("Buku berhasil ditambahkan.")

    def cari_buku(self, nama_buku):
        if nama_buku in self.buku:
            buku = self.buku[nama_buku]
            print('=====PERPUSTAKAAN ITH=====')
            print('Nama Buku: ', nama_buku)
            print('Nama Penulis: ', buku['Penulis'])
            print('Nama Penerbit: ', buku['Penerbit'])
            print('Tahun Terbit: ', buku['Tahun Terbit'])
            print('Jenis Buku: ', buku['Jenis Buku'])
            print('Ketersediaan: ', buku['Ketersediaan'])
            print('Letak Buku (Rak)', buku['Letak Buku'])
            return 'Buku ditemukan'
        else:
            return "Buku tidak ditemukan."

    def tandai_buku_dibaca(self, nama_buku):
        if nama_buku in self.buku:
            self.buku[nama_buku]['Dibaca'] = True
            self.buku_dibaca[nama_buku] = self.buku_dibaca.get(nama_buku, 0) + 1
            print("Buku telah ditandai sebagai sudah dibaca.")
        else:
            print("Buku tidak ditemukan.")

    def buku_teratas(self, n=3):
        sorted_buku = sorted(self.buku_dibaca.items(), key=lambda x: x[1], reverse=True)
        print(f"{n} buku teratas yang paling sering dibaca:")
        for i in range(min(n, len(sorted_buku))):
            buku = sorted_buku[i]
            print(f"{i+1}. {buku[0]} ({buku[1]} kali dibaca)")


perpustakaan_ith = PerpustakaanITH()


def opsi():
    while True:
        print('''
        DAFTAR PELAYANAN PERPUSTAKAAN ITH
        1. TAMBAHKAN BUKU
        2. CARI BUKU
        3. TANDAI BUKU SEBAGAI TELAH DIBACA
        4. TAMPILKAN 3 BUKU TERATAS
        5. KELUAR
        ''')
        menu = input('Masukkan Pilihan: ')
        if menu == '1':
            nama = input('Masukkan Nama Buku: ')
            penulis = input('Masukkan Nama Penulis: ')
            penerbit = input('Masukkan Penerbit Buku: ')
            tahunTerbit = input('Masukkan Tahun Terbit: ')
            jenisBuku = input('Masukkan Jenis Buku: ')
            KetersediaanBuku = input('Masukkan Ketersediaan Buku: ')
            letakBuku = input('Masukkan Letak Buku (Rak): ')

            perpustakaan_ith.tambah_buku(nama, penulis, penerbit, tahunTerbit, jenisBuku, KetersediaanBuku, letakBuku)
            input('Tekan Enter Untuk Kembali')
            os.system('cls')
        elif menu == '2':
            cari = input('Masukkan Nama Buku: ')
            print(perpustakaan_ith.cari_buku(cari))
            input('Tekan Enter Untuk Kembali')
            os.system('cls')        
        elif menu == '3':
            tandai = input('Masukkan Nama Buku yang Dibaca: ')
            perpustakaan_ith.tandai_buku_dibaca(tandai)
            input('Tekan Enter Untuk Kembali')
            os.system('cls')        
        elif menu == '4':
            perpustakaan_ith.buku_teratas(3)
            input('Tekan Enter Untuk Kembali')
            os.system('cls')        
        elif menu == '5':
            os.system('cls')
            print('Terimakasih Sudah Menggunakan Pelayanan Kami') 
            break
        else:
            os.system('cls')
            print('MASUKKAN INPUT DENGAN BENAR!!!')

opsi()




