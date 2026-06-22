def generate_square_pattern(rows: int, cols: int) -> str:
    line = '*' * cols
    return '\n'.join([line for _ in range(rows)])

if __name__ == '__main__':
    print(generate_square_pattern(10, 10))