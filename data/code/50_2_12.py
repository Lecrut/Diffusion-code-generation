def print_centered_triangle(levels):
    for i in range(1, levels + 1):
        stars = '*' * (2 * i - 1)
        width = 2 * levels - 1
        print(stars.center(width))

if __name__ == '__main__':
    print_centered_triangle(12)