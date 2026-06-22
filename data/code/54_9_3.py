def hollow_square_generator(size):
    if size <= 0:
        return
    if size == 1:
        yield "*"
        return
    first_last = "*" * size
    middle = "*" + " " * (size - 2) + "*"
    yield first_last
    for _ in range(size - 2):
        yield middle
    yield first_last

if __name__ == '__main__':
    sample_size = 5
    for row in hollow_square_generator(sample_size):
        print(row)