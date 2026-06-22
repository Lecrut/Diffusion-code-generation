def generate_square_pattern(size=8):
    return ['*' * size for _ in range(size)]

if __name__ == '__main__':
    pattern = generate_square_pattern()
    for row in pattern:
        print(row)