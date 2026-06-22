def print_downward_triangle(rows):
    for i in range(rows, 0, -1):
        print('*' * i)

if __name__ == '__main__':
    n = 9
    result = print_downward_triangle(n)
    print(result)