def print_reverse_number_triangle(n: int) -> None:
    for i in range(1, n + 1):
        for j in range(1, i):
            print(' ', end='')
        for j in range(i, 0, -1):
            print(j, end='')
        for j in range(2, i + 1):
            print(j, end='')
        print()
if __name__ == '__main__':
    n = 5
    print_reverse_number_triangle(n)