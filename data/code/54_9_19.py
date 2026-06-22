def hollow_square_generator(n):
    if n <= 0:
        return
    if n == 1:
        yield "*"
        return
    yield "*" + " " * (n - 2) + "*"
    for _ in range(n - 2):
        yield " " + " " * (n - 2) + " "
    yield "*" + " " * (n - 2) + "*"

if __name__ == '__main__':
    side_length = 7
    for row in hollow_square_generator(side_length):
        print(row)