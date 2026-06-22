def generate_square_pattern(n):
    return ['*' * n for _ in range(n)]

if __name__ == '__main__':
    n = 8
    pattern = generate_square_pattern(n)
    for row in pattern:
        print(row)