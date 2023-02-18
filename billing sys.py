TOT = 0

f = open("C:/Users/Maneth Thimasha/Desktop/mark_clac/bill.txt","a")
f.write("        ********BILLING SYSTEM********"+"\n")
f.write("_________________________________________________"+"\n")

cusID = input("Enter Customer ID: ")
f.write("CUSTOMER ID: " + cusID+"\n")
f.write("Item"+"\t\t"+"Price"+"\t\t"+"Quantity"+"\t\t"+"Total"+"\n")

while True:
    item = input("Enter Item Name: ")
    if item =="":
        break
    prz = input("Enter Item Price: ")
    Q = input("Enter Quantity: ")
    tot = int(prz)*int(Q)
    TOT = TOT +tot
    f.write(item+"\t\t\t"+str(prz)+"\t\t\t"+str(Q)+"\t\t\t\t"+str(tot)+"\n")

f.write("Total Price: "+ str(TOT)+"\n")
f.write("_________________________________________________"+"\n")

f.close()
