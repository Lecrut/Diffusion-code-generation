def print_diamond(n: int) -> None:
    top_half = []
    for i in range(n):
        spaces = " " * (n - i - 1)
        stars = "*" * (2 * i + 1)
        top_half.append(spaces + stars)
    bottom_half = []
    for i in range(n - 2, -1, -1):
        spaces = " " * (n - i - 1)
        stars = "*" * (2 * i + 1)
        bottom_half.append(spaces + stars)
    diamond = top_half + bottom_half
    for line in diamond:
        print(line)

if __name__ == '__main__':
    print_diamond(6)