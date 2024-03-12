print('Sum of all Even Numbers between 1 to 100 !')

s = 0
for i in range(1, 101):
    if i % 2 == 0:
        # print(i)
        s += i
print(f'The sum of the even numbers is {s}')
