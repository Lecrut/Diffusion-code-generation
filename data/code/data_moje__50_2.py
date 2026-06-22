def print_centered_triangle(levels):
    for i in range(1, levels + 1):
        stars = ' *' * i
        print(stars.center(levels * 2 - 1))

if __name__ == '__main__':
    print_centered_triangle(12)