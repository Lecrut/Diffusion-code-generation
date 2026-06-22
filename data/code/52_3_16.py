def print_diamond(n):
    upper_half = []
    for i in range(n):
        spaces = " " * (n - i - 1)
        stars = "*" * (2 * i + 1)
        upper_half.append(spaces + stars)
    lower_half = []
    for i in range(n - 2, -1, -1):
        spaces = " " * (n - i - 1)
        stars = "*" * (2 * i + 1)
        lower_half.append(spaces + stars)
    full_diamond = upper_half + lower_half
    for line in full_diamond:
        print(line)

if __name__ == '__main__':
    print_diamond(6)