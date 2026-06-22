def hollow_square_rows(n: int):
    if n <= 0:
        return
    if n == 1:
        yield '#'
        return
    top_bottom = '#' * n
    middle = '#' + ' ' * (n - 2) + '#'
    for i in range(n):
        if i == 0 or i == n - 1:
            yield top_bottom
        else:
            yield middle
if __name__ == '__main__':
    size = 5
    rows = list(hollow_square_rows(size))
    for row in rows:
        print(row)