def print_inverted_triangle(height):
    for i in range(height, 0, -1):
        print('*' * i)

if __name__ == '__main__':
    print_inverted_triangle(5)