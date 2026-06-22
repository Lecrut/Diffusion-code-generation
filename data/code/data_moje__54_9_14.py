def hollow_square_generator(n):
    if n <= 0:
        return
    if n == 1:
        yield '*'
        return
    first_last_row = '*' * n
    middle_row = '*' + ' ' * (n - 2) + '*'
    yield first_last_row
    for _ in range(n - 2):
        yield middle_row
    if n > 1:
        yield first_last_row

if __name__ == '__main__':
    n = 5
    result = list(hollow_square_generator(n))
    for line in result:
        print(line)