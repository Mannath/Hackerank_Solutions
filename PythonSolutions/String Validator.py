s = input()
c1=0
c2=0
c3=0
c4=0
c5=0
for i in s:
    if(i.isalnum()):
        c1=1
    if(i.isalpha()):
        c2=1
    if i.isdigit():
        c3=1
    if i.islower():
        c4=1
    if i.isupper():
        c5=1
if c1==1:
    print(True)
else:
    print(False)
if c2==1:
    print(True)
else:
    print(False)
if c3==1:
    print(True)
else:
    print(False)
if c4==1:
    print(True)
else:
    print(False)
if c5==1:
    print(True)
else:
    print(False)