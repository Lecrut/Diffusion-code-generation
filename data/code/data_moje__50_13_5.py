def print_inverted_triangle(rows):
    for i in range(rows, 0, -1):
        print('*' * i)

if __name__ == '__main__':
    sample_size = 5
    print_inverted_triangle(sample_size)