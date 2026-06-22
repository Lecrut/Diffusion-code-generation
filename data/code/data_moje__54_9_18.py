def hollow_square(n):
    if n <= 0:
        return
    if n == 1:
        yield '*'
        return
    top_bottom = '*' * n
    middle = '*' + ' ' * (n - 2) + '*'
    yield top_bottom
    for _ in range(n - 2):
        yield middle
    yield top_bottom

if __name__ == '__main__':
    n = 5
    result = list(hollow_square(n))
    for row in result:
        print(row)