def buat_tabel(kunci):
    kunci = kunci.upper().replace('J', 'I')  # Mengganti J dengan I dan mengubah menjadi huruf besar
    alfabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    tabel = ''
    for char in kunci + alfabet:
        if char not in tabel:
            tabel += char
    return tabel

def buat_teks(teks):
    teks = teks.upper().replace('J', 'I')  # Mengganti J dengan I dan mengubah menjadi huruf besar
    teks = ''.join(filter(str.isalpha, teks))  # Menghapus karakter non-abjad
    if len(teks) % 2 != 0:
        teks += 'X'  # Membuat panjangnya menjadi genap
    return teks

def enkripsi(plaintext, kunci):
    tabel = buat_tabel(kunci)
    plaintext = buat_teks(plaintext)
    sandi = ''
    for i in range(0, len(plaintext), 2):
        a, b = plaintext[i], plaintext[i + 1]
        a_baris, a_kolom = divmod(tabel.index(a), 5)
        b_baris, b_kolom = divmod(tabel.index(b), 5)
        if a_baris == b_baris:
            a_kolom = (a_kolom + 1) % 5
            b_kolom = (b_kolom + 1) % 5
        elif a_kolom == b_kolom:
            a_baris = (a_baris + 1) % 5
            b_baris = (b_baris + 1) % 5
        else:
            a_kolom, b_kolom = b_kolom, a_kolom
        sandi += tabel[a_baris * 5 + a_kolom] + tabel[b_baris * 5 + b_kolom]
    return sandi

def dekripsi(sandi, kunci):
    tabel = buat_tabel(kunci)
    sandi = buat_teks(sandi)
    plaintext = ''
    for i in range(0, len(sandi), 2):
        a, b = sandi[i], sandi[i + 1]
        a_baris, a_kolom = divmod(tabel.index(a), 5)
        b_baris, b_kolom = divmod(tabel.index(b), 5)
        if a_baris == b_baris:
            a_kolom = (a_kolom - 1) % 5
            b_kolom = (b_kolom - 1) % 5
        elif a_kolom == b_kolom:
            a_baris = (a_baris - 1) % 5
            b_baris = (b_baris - 1) % 5
        else:
            a_kolom, b_kolom = b_kolom, a_kolom
        plaintext += tabel[a_baris * 5 + a_kolom] + tabel[b_baris * 5 + b_kolom]
    return plaintext

if __name__ == '__main__':
    print ('-----------------------------------')
    print ('    Nama        : Munis Zulhusni   ')
    print ('    Nim         : A11.2021.13693   ')
    print ('    Kelas       : A11.4302         ')
    print ('-----------------------------------')   

    option = int (input ('1. Enkripsi\n2. Deskripsi\nPilih Option                     : '))
    if option == 1:
        plaintext = input('Masukkan pesan (Plaintext)       : ')
        kunci = input('Masukkan kunci                   : ')
        sandi = enkripsi(plaintext, kunci)
        print('Teks terenkripsi                 : ', sandi)
        
    elif option == 2:
        sandi = input('Masukkan pesan (Chipertext)      : ')
        kunci = input('Masukkan kunci                   : ')
        plaintext = dekripsi(sandi, kunci)
        print('Teks terdekripsi                 : ', plaintext)
        
    else:
         print ('TIDAK VALID! PILIH OPSI LAIN!') 
