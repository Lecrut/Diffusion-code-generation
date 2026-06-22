def generate_square_pattern(size):
    return [("*" * size) for _ in range(size)]

if __name__ == '__main__':
    pattern = generate_square_pattern(10)
    for row in pattern:
        print(row)