def print_reverse_triangle(rows):
    for i in range(rows, 0, -1):
        print(' '.join(str(j) for j in range(i, 0, -1)))

if __name__ == '__main__':
    print_reverse_triangle(6)