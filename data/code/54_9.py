def hollow_square_generator(n):
    if n <= 0:
        return
    if n == 1:
        yield '*'
        return
    first_last_row = '*' * n
    middle_row = '*' + ' ' * (n - 2) + '*'
    for i in range(n):
        if i == 0 or i == n - 1:
            yield first_last_row
        else:
            yield middle_row

if __name__ == '__main__':
    n = 5
    generator = hollow_square_generator(n)
    for row in generator:
        print(row)