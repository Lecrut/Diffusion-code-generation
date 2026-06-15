def print_star_pattern(n):
    for i in range(n):
        spaces = " " * (n - 1 - i)
        stars = "*" * (2 * n - 1 - 2 * i)
        print(spaces + stars)
if __name__ == '__main__':
    print_star_pattern(5)
    print("-" * 10)
    print_star_pattern(8)