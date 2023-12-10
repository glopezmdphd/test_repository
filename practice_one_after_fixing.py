#find three different ways to print the number 0 thru 10 using Python.
for i in range(11):
    print(i)

i = 0
while i <= 10:
    print(i)
    i += 1

numbers = list(range(11))
print(' '.join(map(str, numbers)))
