def print_right_angled_triangle(rows):
    for i in range(1, rows + 1):
        for j in range(i):
            print('*', end='')
        print()

if __name__ == '__main__':
    print_right_angled_triangle(5)