def print_star_triangle(levels):
    for i in range(1, levels + 1):
        spaces = ' ' * (levels - i)
        stars = '*' * (2 * i - 1)
        print(f"{spaces}{stars}")

if __name__ == '__main__':
    print_star_triangle(12)