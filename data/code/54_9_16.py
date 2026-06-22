def hollow_square_generator(size):
    if size <= 0:
        return
    if size == 1:
        yield "*"
        return
    yield "*" * size
    for _ in range(size - 2):
        yield "*" + " " * (size - 2) + "*"
    yield "*" * size

if __name__ == '__main__':
    size = 5
    generator = hollow_square_generator(size)
    for row in generator:
        print(row)