#While Loop
#Catatan: Penentuan ruang lingkup di Python bisa menggunakan tab alih-alih menggunakan tanda kurung

count = 0
while (count < 9):
  print ("The count is: ", count)
  count = count + 1

print ("Good bye!")

# For Loop
angka = [1,2,3,4,5]
for x in angka:
  print(x)

#Contoh pengulangan for
buah = ["nanas", "apel", "jeruk"]
for makanan in buah:
  print ("Saya suka makan", makanan)


# Nested Loop
i = 2
while(i < 100):
    j = 2
    while(j <= (i/j)):
        if not(i%j): break
        j = j + 1
        if (j > i/j) : print(i, " is prime")
        i = i + 1

print("Good bye!")