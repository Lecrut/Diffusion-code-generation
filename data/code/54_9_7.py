def hollow_square_rows(n):
    if n <= 0:
        return
    if n == 1:
        yield "*"
        return
    yield "*" + " " * (n - 2) + "*"
    for _ in range(n - 2):
        yield "*" + " " * (n - 2) + "*"
    yield "*" * n

if __name__ == '__main__':
    sample_n = 7
    for row in hollow_square_rows(sample_n):
        print(row)