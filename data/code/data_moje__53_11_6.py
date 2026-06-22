def print_reverse_number_triangle(height: int) -> None:
    for row in range(height, 0, -1):
        line = ''.join(str(num) for num in range(1, row + 1))
        print(line)

if __name__ == '__main__':
    sample_height = 5
    print_reverse_number_triangle(sample_height)