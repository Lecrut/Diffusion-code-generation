def print_reverse_number_triangle(rows: int) -> None:
    for i in range(rows, 0, -1):
        print(' '.join(str(num) for num in range(1, i + 1)))

if __name__ == '__main__':
    sample_rows = 5
    print_reverse_number_triangle(sample_rows)