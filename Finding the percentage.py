import sys

n = int(input())
avg = 0
values = []
names = []

if not (1 <= n <= 100):
    sys.exit()

for i in range(n):
    values_string = input().split()
    names.append(values_string[0])
    values_local = [float(val) for val in values_string[1:]]

    for mark in values_local:
       if not (0 <= mark <= 100):
           sys.exit()

    values.append(values_local)

name = input()

if name in names:
    index = names.index(name)
    avg = sum(values[index]) / len(values[index])
    print(f"{avg:.2f}")
else:
     sys.exit()
