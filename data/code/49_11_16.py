def generate_square_pattern(size: int) -> list[str]:
    return ["*" * size for _ in range(size)]

if __name__ == '__main__':
    pattern = generate_square_pattern(10)
    for line in pattern:
        print(line)