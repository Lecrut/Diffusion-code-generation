def print_star_pyramid(n):
    if n <= 0:
        return
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * (2 * i - 1))

if __name__ == '__main__':
    pyramid_height = 3
    print_star_pyramid(pyramid_height)