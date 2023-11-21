#open an existing file for read operation
file = open("name.txt", "r") 
print (file.read())
#To overwrite an existing data
# file = open("name.txt", "w") 
# file.write("I am sai eashwar")
# file.close()
#To append an existing file and it won't overwrite 
# file = open("name.txt", "a") 
# file.write("\nThis will add this line")
# file.close()
#To append and open a existing file and it won't overwrite
file = open("name.txt", "a+") 
file.write("\nThis will add this line")
file.close()
