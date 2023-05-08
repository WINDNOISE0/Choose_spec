a = []
b = []

while True:
    value = input("Введите строку ")
    if value == "stop":
        break
    a.append(value)

for i in range(len(a)):
    if len(a[i]) <= 3:
        b.append(a[i])

print(b)