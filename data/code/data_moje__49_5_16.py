def print_square_pattern(size):
    return ["*" * size for _ in range(size)]

if __name__ == "__main__":
    dimension = 8
    pattern = print_square_pattern(dimension)
    for row in pattern:
        print(row)