def generate_square_pattern(size: int) -> str:
    line = '*' * size
    return '\n'.join([line] * size)

if __name__ == '__main__':
    print(generate_square_pattern(6))