def print_star_triangle(rows):
    for i in range(1, rows + 1):
        for j in range(i):
            print('*', end='')
        print()

if __name__ == '__main__':
    num_rows = 5
    print_star_triangle(num_rows)