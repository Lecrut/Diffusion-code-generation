def print_diamond_pattern(rows: int) -> None:
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '*' * (2 * i - 1))
    for i in range(rows - 1, 0, -1):
        print(' ' * (rows - i) + '*' * (2 * i - 1))

if __name__ == '__main__':
    sample_rows = 5
    print_diamond_pattern(sample_rows)