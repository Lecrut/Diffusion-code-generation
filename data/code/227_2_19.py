def print_inverted_right_triangle(rows):
    for i in range(rows, 0, -1):
        print('*' * i)

if __name__ == '__main__':
    sample_rows = 7
    print_inverted_right_triangle(sample_rows)