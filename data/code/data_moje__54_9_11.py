def hollow_square_generator(n):
    if n < 1:
        return
    row0 = '*' * n
    yield row0
    if n == 1:
        return
    if n == 2:
        yield row0
        return
    middle_row = '*' + ' ' * (n - 2) + '*'
    for _ in range(n - 2):
        yield middle_row
    yield row0

if __name__ == '__main__':
    result = list(hollow_square_generator(5))
    for line in result:
        print(line)