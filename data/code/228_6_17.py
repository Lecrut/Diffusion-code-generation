def print_pyramid(n):
    if n <= 0:
        return
    else:
        print(' ' * (n - 1) + '*' * (2 * n - 1))
        print_pyramid(n - 1)

if __name__ == '__main__':
    height = 5
    print_pyramid(height)