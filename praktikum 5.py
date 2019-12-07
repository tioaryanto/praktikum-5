#Dictonary
#Daftar nilai mahasiswa

#tambah data
data = {}
while True:
    print ("\\<><><><><><><><><><><><><><>DATA NILAI AKHIR MAHASISWA<><><><><><><><><></")
    print ("****************************************************************************")    
    print ("============================================================================")
    print (" |  No |   Nama   |     NIM     |  Tugas |   UTS  |   UAS  |  NILAI |" )
    print ("============================================================================")
    b = input("(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar,: ")
    if b.lower() == 'k':
        break
    elif b.lower() == 't':
        print(" Tambah Data ")
        nama = input(" Nama: ")
        nim = input(" NIM:")
        nilaiuts = int(input (" Nilai UTS     : "))
        nilaiuas = int(input (" Nilai UAS     : "))
        nilaitgs = int(input (" Nilai Tugas   : "))
        akhir = ((nilaitgs)*30/100 + (nilaiuts)*35/100 + (nilaiuas)*35/100)
        data[nama] = nim, nilaiuts, nilaiuas, nilaitgs, akhir    
        print("")
    elif b.lower() == 'l':
        if data.items():
            print ("daftar data nilai mahasiswa")
            print ("\\<><><><><><><><><><><><><DATA NILAI AKHIR MAHASISWA<><><><><><><>></")
            print ("**********************************************************************")    
            print ("======================================================================")
            print (" |  No |   Nama   |     NIM     |  Tugas |   UTS  |   UAS  |  NILAI |" )
            print ("======================================================================") 
            i=0
            for x in data.items():
                i+=1
                print(" |  {6:2d} | {0:16s}  | {1:9s} | {2:5} | {3:3} | {4:3} | {5:2.2f} |"\
                      .format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))
        else:
            print ("\\<><><><><><><><><><>DATA NILAI AKHIR MAHASISWA><><><><><><><><><>></")
            print ("**********************************************************************")    
            print ("======================================================================")
            print (" |  No |   Nama   |     NIM     |  Tugas |   UTS  |   UAS  |  NILAI |" )
            print ("======================================================================")
            print (" |                      Tidak Ada Daftar Nilai                        ")
            print ("======================================================================")
    elif b.lower() == 'h':
        print(" Hapus Daftar Nilai Mahasiswa ")
        nama = input("Masukan Nama : ")
        if nama in data.keys():
            del data[nama]
            print("")
        else:
            print("data {0} tidak ada".format(nama))
            print("")
    elif b.lower() == 'c':
        print("cari data mahasiswa") 
        nama = input("Nama Mahasiswa: ")
        if nama in data.keys():
            print ("\\-----------------DATA NILAI AKHIR MAHASISWA----------------------/")
            print ("********************************************************************")
            print ("====================================================================")
            print (" |   Nama   |     NIM     |  Tugas |   UTS  |   UAS  |  NILAI |" )
            print ("====================================================================")
            print (" Data Nilai {0} adalah ('nim', Tugas, UTS, UAS, Akhir ) => {1}"\
                   .format(nama, data [nama])) 
            print  ("====================================================================")
            print("")
    elif b.lower() == 'u':
        print(" Ubah Daftar Nilai Mahasiswa ")
        nama = input("Masukan Nama mahasiswa : ")
        if nama in data.keys():
            nim = input(" NIM:")
            nilaiuts = int(input (" Nilai UTS     : "))
            nilaiuas = int(input (" Nilai UAS     : "))
            nilaitgs = int(input (" Nilai Tugas   : "))
            akhir = ((nilaitgs)*30/100 + (nilaiuts)*35/100 + (nilaiuas)*35/100)
            data[nama] = nim, nilaiuts, nilaiuas, nilaitgs, akhir    
            print("")
        else:
            print ("====================================================================")
            print ("Daftar Nilai {0} tidak ada ".format(nama))        
            print ("====================================================================")
            print ("")
    else:
        print ("pilih menu yang tersedia")
        print ("")
    
    
        
