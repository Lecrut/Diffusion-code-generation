def print_star_square(size=12):
    line = "* " * size
    rows = [line for _ in range(size)]
    return "\n".join(rows)

if __name__ == '__main__':
    print(print_star_square(12))