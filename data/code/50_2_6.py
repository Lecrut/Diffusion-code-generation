def print_centered_triangle(levels: int) -> None:
    stars = [('*' * (2 * i + 1)).center(2 * levels - 1) for i in range(levels)]
    for line in stars:
        print(line)

if __name__ == '__main__':
    print_centered_triangle(12)