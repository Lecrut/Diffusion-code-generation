def print_star_pyramid(height):
    for i in range(1, height + 1):
        print(" " * (height - i) + "* " * (2 * i - 1))

if __name__ == '__main__':
    print_star_pyramid(3)