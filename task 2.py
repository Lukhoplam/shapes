shape=input(str("choose shape number of the building you want \n 1.square\n2.rectangular\n3.round\n")).lower()


pi_=3.142

print()
if shape=="1" :
    length=(float(input(" what is the length of the building?")))
    print(length**2)

elif shape=='2':
    width=(float(input("what is the width of the building ?")))
    length=(float(input(" what is the length of the building?")))
    print(length*width)

else:
    shape=='3'
    raduis=(float(input('what is the radius ?')))
    
    print(pi_*(raduis**2))
    
    



    


