def generate_square_pattern(size: int) -> str:
    row = '*' * size + '\n'
    return row * size

if __name__ == '__main__':
    size = 6
    print(generate_square_pattern(size), end='')