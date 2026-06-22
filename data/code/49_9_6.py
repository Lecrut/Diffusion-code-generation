def print_star_square(size=12):
    row = "* " * size
    lines = [row for _ in range(size)]
    return "\n".join(lines)

if __name__ == '__main__':
    print(print_star_square())