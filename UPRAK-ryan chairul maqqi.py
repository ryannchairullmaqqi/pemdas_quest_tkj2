print("1. Balok")

panjang = int(input("masukan nilai panjang"))
lebar = int(input("masukan nilai lebar"))
tinggi = int(input("masukan nilai tinggi"))

volume_bal = panjang * lebar * tinggi
print("Nilai volume balok adalah", volume_bal)

print("\n2. tabung")

luas_alas_lingkaran = int(input("masukan nilai luas alas lingkaran"))
tinggi = int(input("masukan nilai tinggi"))

volume_ling = luas_alas_lingkaran * tinggi
print("nilai volume tabung adalah", volume_ling)

print("\n3. Limas")

luas_alas_persegi = int(input("masukan nilai Luas alas persegi"))
tinggi = int(input("masukkan nilai tinggi"))
volume_lim = (1/3 * luas_alas_persegi) * tinggi

print("\n4. konversi dollar")

x = int(input("Masukan nilai dollar"))
y = x * 14000
print(x, "dollar =", y, "rupiah")