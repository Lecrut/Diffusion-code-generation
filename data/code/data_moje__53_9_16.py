def print_reverse_number_triangle(height=5):
    for i in range(height, 0, -1):
        print(' '.join(str(i) for _ in range(i)))

if __name__ == '__main__':
    print_reverse_number_triangle()