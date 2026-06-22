def print_triangle(height):
    for i in range(1, height + 1):
        print('*' * i)

if __name__ == '__main__':
    sample_height = 5
    print_triangle(sample_height)