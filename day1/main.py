data = open("input.txt", "r").read().splitlines()
a = []
final = 0
for line in data :
    for element in line :
        if element.isdigit() :
            a.append(int(element))
    total = str(a[0]) +  str(a[-1])
    final += int(total)
    a=[]
print(final)