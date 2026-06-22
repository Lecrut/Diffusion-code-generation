def print_reverse_number_triangle(n):
    for i in range(n, 0, -1):
        print(*(range(1, i + 1)))

if __name__ == '__main__':
    print_reverse_number_triangle(5)