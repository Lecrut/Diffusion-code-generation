def print_downward_triangle():
    rows = 9
    for i in range(rows, 0, -1):
        print('*' * i)

if __name__ == '__main__':
    print_downward_triangle()