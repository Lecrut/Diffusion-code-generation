def print_star_pyramid(n):
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "* " * (2 * i - 1)
        print(spaces + stars)

if __name__ == '__main__':
    pyramid_height = 3
    print_star_pyramid(pyramid_height)