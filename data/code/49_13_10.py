def generate_square_pattern(size: int) -> str:
    row = '*' * size
    return '\n'.join([row] * size)

if __name__ == '__main__':
    print(generate_square_pattern(6))