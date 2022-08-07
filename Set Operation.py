print("...😎 Welcome to Set Operation Executer😎...")
set1=set()
set2=set()
name1=str(input("Enter the name of the 1 Set:"))
while True:
    n=input("Enter element for"  +" " + str(name1) +" " + ":")
    if n=="done":
        break
    set1.add(n)

print(f"{name1}" + ":" + str(set1))

name2=input("Enter the name of the 2 Set:")
while True:
    m=input("Enter element for"  +" " + str(name2) +" " + ":")
    if m=="done":
        break
    set2.add(m)

print(f"{name2}" + ":"+ str(set2))

while True:
    print("Want to start📝..?")
    x=input("Say 'yes'🙋 or 'no'🙅:")
    if x=="yes":
        print("Okkk..lets go🚝🛺")
    else:
        break
    print("What operation you want to do with your sets👀?")
    print(".....Choose  from the below list....")
    list=["1.Add elements","2.Remove elements","3.Empty sets","4.Union","5.Intersection","6.Difference","7.Symmetric difference"]
    for i in list:
       print(i)
    k=int(input("Enter a number between '1' —→'7':"))
    if k==1:
        a=int(input("For " + str(name1) + " enter '1' : And For "+ str(name2) +" enter '2':"))
        if a==1:
            while True:
                b=input("Enter element for" + " " +str(name1)+ ":")
                if b=="done":
                    break
                set1.add(b)
            print(str(name1) + ":" + str(set1))
        else:
            while True:
                c=input("Enter element for" + " " +str(name2)+ ":")
                if c=="done":
                    break
                set2.add(c)
            print(str(name2) + ":" + str(set2))
    elif k==2:
        d=int(input("For " + str(name1) + " enter '1' : And For "+ str(name2) +" enter '2':"))
        if d==1:
            while True:
                e=input("Enter  the element to remove from" + " " +str(name1)+ ":")
                if e=="done":
                    break
                set1.remove(e)
            print(str(name1) + ":" + str(set1))
        else:
            while True:
                f=input("Enter the  element to remove from" + " " +str(name2)+ ":")
                if f=="done":
                    break
                set2.remove(f)
            print(str(name2) + ":" + str(set2))
    elif k==3:
        g=int(input("For " + str(name1) + " enter '1' : And For "+ str(name2) +" enter '2':"))
        if g==1:
            set1.clear()
            print(str(name1) + ":" + str({}))
        else:
            set2.clear()
            print(str(name2) + ":" + str({}))
    elif k==4:
        h=set1|set2
        print("The Union of " + str(set1) + " & " + str(set2) + " is: " + str(h))
    elif k==5:
        j=set1 & set2
        print("The Intersection  of " + str(set1) + " & " + str(set2) + " is: " + str(j))
    elif k==6:
        z=int(input("For difference between " + str(name1)+ " & "+ str(name2) + " enter '1' And for difference between " + str(name2)+" & " + str(name1) +" enter '2'"))
        if z==1:
            l=set1 -set2
            print("The Difference of " + str(set1) + " & " + str(set2) + " is: " + str(l))
        else:
            y=set2 -set1
            print("The Difference of " + str(set2) + " & " + str(set1) + " is: " + str(y))
    elif k==7:
        o=set1 ^ set2
        print("The Symmetrical Difference of " + str(set1) + " & " + str(set2) + " is: " + str(o))
    else:
        print("Please enter a valid option....")
   



    



    

       
