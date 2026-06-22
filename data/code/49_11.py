def generate_square_pattern(size: int, char: str) -> list:
    return [[char for _ in range(size)] for _ in range(size)]

if __name__ == '__main__':
    size = 10
    pattern = generate_square_pattern(size, '*')
    for row in pattern:
        print(''.join(row))