def print_square_pattern(size=8):
    return [''.join(['*' for _ in range(size)]) for _ in range(size)]

if __name__ == '__main__':
    result = print_square_pattern()
    for row in result:
        print(row)