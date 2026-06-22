def print_reverse_number_triangle(height: int) -> None:
    for row in range(height, 0, -1):
        print(' '.join(str(num) for num in range(row, 0, -1)))

if __name__ == '__main__':
    print_reverse_number_triangle(5)