def generate_square_pattern(rows: int, cols: int) -> str:
    return '\n'.join(['* ' * cols for _ in range(rows)])

if __name__ == '__main__':
    result = generate_square_pattern(10, 10)
    print(result)