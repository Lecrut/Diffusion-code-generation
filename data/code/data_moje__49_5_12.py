def print_square_pattern(size):
    return [''.join(['*' for _ in range(size)]) for _ in range(size)]

if __name__ == '__main__':
    size = 8
    pattern = print_square_pattern(size)
    for row in pattern:
        print(row)