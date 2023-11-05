file=open("liczby.txt", "r")
numbers=list(map(str.strip, file.readlines()))
morezero=[]
for number in numbers:
    I=0
    O=0
    for i in number:
        if int(i)==1:
            I+=1
        else:
            O+=1
    if O>I:
        morezero.append(number)
print(len(morezero))
numbersint=[]
for number in numbers:
    numbersint.append(int(number, 2))
d2=0
d8=0
for i in numbersint:
    if i%2==0:
        d2+=1
    if i%8==0:
        d8+=1
print(d2, d8)
smallest_num=numbersint[0]
biggest_num=numbersint[0]
for i in numbersint:
    if i<smallest_num:
        smallest_num=i
    if i>biggest_num:
        biggest_num=i
print(numbersint.index(smallest_num)+1)
print(numbersint.index(biggest_num)+1)
