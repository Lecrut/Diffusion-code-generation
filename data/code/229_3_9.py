def generate_square(size):
    row = '*' * size
    return [row for _ in range(size)]

if __name__ == '__main__':
    square_size = 8
    grid = generate_square(square_size)
    for line in grid:
        print(line)