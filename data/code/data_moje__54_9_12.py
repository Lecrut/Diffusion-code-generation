def hollow_square_generator(n):
    if n <= 0:
        return
    if n == 1:
        yield "*"
        return
    for i in range(n):
        if i == 0 or i == n - 1:
            yield "*" * n
        else:
            yield "*" + " " * (n - 2) + "*"

if __name__ == "__main__":
    size = 5
    for row in hollow_square_generator(size):
        print(row)