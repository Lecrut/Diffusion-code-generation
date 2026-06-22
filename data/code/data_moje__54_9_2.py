def hollow_square_generator(n):
    if n <= 0:
        return
    if n == 1:
        yield '*'
        return
    yield '*' * n
    for _ in range(n - 2):
        yield '*' + ' ' * (n - 2) + '*'
    yield '*' * n

if __name__ == '__main__':
    n = 5
    result = list(hollow_square_generator(n))
    for row in result:
        print(row)