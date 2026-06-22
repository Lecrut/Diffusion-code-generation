def hollow_square_generator(n):
    if n <= 0:
        return
    if n == 1:
        yield "*"
        return
    if n == 2:
        yield "**"
        yield "**"
        return
    yield "*" * n
    for _ in range(n - 2):
        yield "*" + " " * (n - 2) + "*"
    yield "*" * n

if __name__ == '__main__':
    size = 7
    for row in hollow_square_generator(size):
        print(row)