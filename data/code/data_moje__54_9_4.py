def generate_hollow_square(n):
    if n <= 0:
        return
    if n == 1:
        yield '*'
        return
    top_row = '*' * n
    yield top_row
    if n > 2:
        middle_row = '*' + ' ' * (n - 2) + '*'
        for _ in range(n - 2):
            yield middle_row
    if n > 1:
        bottom_row = top_row
        yield bottom_row

if __name__ == '__main__':
    n = 5
    for row in generate_hollow_square(n):
        print(row)