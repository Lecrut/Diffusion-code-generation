def print_hollow_square(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print('*' * n)
        else:
            print('*' + ' ' * (n - 2) + '*')

if __name__ == '__main__':
    size = 6
    print_hollow_square(size)