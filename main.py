f1= open('do.txt', 'r')
f2=open('re.txt' , 'w')

count=f1.readlines()
for i in range(1, len(count) +1):
    if(i % 2 !=0):
        f2.write(count[i-1])
    else:
        pass
f2.close()

f2=open('re.txt' , 'r')
print(f2.read)

f2.close()
f1.close()
