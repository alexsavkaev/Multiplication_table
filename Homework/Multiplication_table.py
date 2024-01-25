def multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i * j < 10:
                print(f'{i}  *  {j} = {i * j}', end='     ')
            else:
                print(f'{i}  *  {j} = {i * j}', end='    ')
        print()


n = int(input('Введите число n: '))
multiplication_table(n)
