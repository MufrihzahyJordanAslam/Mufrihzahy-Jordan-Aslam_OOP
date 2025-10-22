# ====================================================
# Nama : Mufrihzahy Jordan Aslam (24241167)
# Class : SepedaMotor
# Object : surat2, kondisi_mesin, merk, model, harga, cc, warna
# ====================================================

class SepedaMotor:
    def __init__(self, surat2, kondisi_mesin, merk, model, harga, cc, warna):
        self.surat2 = surat2
        self.kondisi_mesin = kondisi_mesin
        self.merk = merk
        self.model = model
        self.harga = int(harga)     # ubah ke integer untuk angka harga
        self.cc = float(cc)         # ubah ke float untuk kapasitas mesin
        self.warna = warna

    def tampilkan_info(self):
        print("=" * 45)
        print("     INFORMASI SEPEDA MOTOR".center(45))
        print("=" * 45)
        print(f"Merk            : {self.merk}")
        print(f"Model           : {self.model}")
        print(f"Warna           : {self.warna}")
        print(f"Kapasitas Mesin : {self.cc} cc")
        print(f"Harga           : Rp{self.harga:,.0f}")
        print(f"Kondisi Mesin   : {self.kondisi_mesin}")
        print(f"Surat-surat     : {self.surat2}")
        print("=" * 45)


# Contoh penggunaan class
motor1 = SepedaMotor(
    surat2="Lengkap (STNK & BPKB)",
    kondisi_mesin="Baik",
    merk="Honda",
    model="Beat Deluxe Smart Key",
    harga=20000000,
    cc=109.5,
    warna="Deluxe Matte Blue"
)

# Menampilkan informasi motor
motor1.tampilkan_info()