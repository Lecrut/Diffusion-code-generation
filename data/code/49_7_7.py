def generate_square_rows(size):
    for _ in range(size):
        yield '*' * size

if __name__ == '__main__':
    size = 3
    square_rows = generate_square_rows(size)
    for row in square_rows:
        print(row)