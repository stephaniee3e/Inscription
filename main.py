name = input ("Whom should I sign to:")
file_name = "inscribed.txt"
f = open (file_name, "w")
with open (file_name, "w") as f:
    f.write ("Hi " + name +"," )
    f.write (" we hope you enjoy learning Python with us!")
    f.write (" Best,")
    f.write (" Th3 3l337 AP Computer Science Team")
    f.close()
with open (file_name) as f:
    print(f.read())
   



