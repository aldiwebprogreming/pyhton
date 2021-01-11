b = "muhammad eldavin malikhi"
#mengjdikkan string hurup kaptital
print(b.upper())

#mengahpus spasi string sebelum dan sesudah
c = " melda lutfiah "
print(c.strip())

#menggabungakan string
gabung = b + " " + c

print(gabung)

#menggabungakan string dengan integer 

txt = "Umur saya adalah {}" 
age = 25
print(txt.format(age))

biodata = "umur saya adalah {}, nomo rumah saya adalah {}, kode pos daerah saya adalah {}"
umur = 25 
no_rumah = 100
kode_pos = 3133

print(biodata.format(umur, no_rumah, kode_pos))


#type data bolean (true and false)

print(10>3)
print(50 < 30)
print(10 ==10 )
print(10 != 10 )


a = 200
b = 33

if a < b:
    print("benar")
else:
        print("salah")


#python list

nama = ["aldi","dahlia","naila","davin"]
print(nama)
print(nama[1])

#mengubah python list 

nama[1] = "budi"

print(nama)

nama[0:1] = ["uje", "faiz"]
print(nama)

#mengahapus value list
nama.remove("uje")
print(nama)

#mengahpus semua value lis
del nama