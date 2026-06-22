def generate_star_pattern(rows: int = 10, cols: int = 10) -> list:
    return ['*' * cols for _ in range(rows)]

if __name__ == '__main__':
    pattern = generate_star_pattern()
    for row in pattern:
        print(row)