a = range(10)
print(list(a))
while a:
    print(a[-1])
    a = a[:len(a)-1]