# Melakukan input user
print('=' * 25)
print('Operasi Matematika')
print(' 1. Jumlah \t [+]')
print(' 2. kurang \t [-]')
print(' 3. kali \t [*]')
print(' 4. bagi \t [/]')
print('=' * 25)
operasi = input('pilih operasi (1/2/3/4): ')
bilangan_1 = eval(input('Masukkan bilangan pertama: '))
bilangan_2 = eval(input('Masukkan bilangan kedua: '))

# Melakukan percabangan atau kondisi
print('=' * 25)


if operasi == '1':
    print('User memilih penjumlahan')
elif operasi == '2':
    print('User memilih pengurangan')
elif operasi == '3':
    print('User memilih perkalian')
elif operasi == '4':
    print('User memilih pembagian')
else:
    print('Data Tidak valid')

# Menghitung hasil operasi

if operasi == '1':
    hasil = bilangan_1 + bilangan_2
    print(f'Hasil operasi dari {bilangan_1} + {bilangan_2} = {hasil}')
elif operasi == '2':
    hasil = bilangan_1 - bilangan_2
    print(f'Hasil operasi dari {bilangan_1} - {bilangan_2} = {hasil}')
elif operasi == '3':
    hasil = bilangan_1 * bilangan_2
    print(f'Hasil operasi dari {bilangan_1} * {bilangan_2} = {hasil}')
elif operasi == '4':
    hasil = bilangan_1 / bilangan_2
    print(f'Hasil operasi dari {bilangan_1} / {bilangan_2} = {hasil}')
else:
    print('Tidak valid')
