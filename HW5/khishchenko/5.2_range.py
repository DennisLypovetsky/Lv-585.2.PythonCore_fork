Even = []
Odd = []
NumbersThatAreNotDivisibleBy2And3 = []

for item in range(1,10):
    if item % 2 == 0:
        Even.append(item)
    if item % 3 == 0:
        Odd.append(item)
    if item % 2 != 0 and  item % 3 != 0:
        NumbersThatAreNotDivisibleBy2And3.append(item)

print("Even numbers:", Even)
print("Odd numbers:", Odd)
print("Not divisibel by 2 and 3:", NumbersThatAreNotDivisibleBy2And3)