def print_inverted_right_triangle(size: int) -> None:
    for row in range(size, 0, -1):
        print('*' * row)

if __name__ == '__main__':
    sample_size = 5
    print_inverted_right_triangle(sample_size)