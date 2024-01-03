 

#Binary Type Data
#bite and bite array range 0-255

mustafalist = [1,2,0,20,50,80,254,255]

b = bytes(mustafalist)
print(type(b))

print(b)

#bytearray .....

mustafalist2 = [1,2,0,20,50,80,254,255]

b1 = bytearray(mustafalist)
print(type(b1))
print(b1)

b1[2]=43

print(b1[2])




