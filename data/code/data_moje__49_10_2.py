def print_square_pattern(side_length: int = 5) -> None:
    pattern = '*' * side_length
    for _ in range(side_length):
        print(pattern)

if __name__ == '__main__':
    print_square_pattern(5)