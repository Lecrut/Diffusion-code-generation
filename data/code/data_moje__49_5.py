def print_square_pattern(size):
    row = "* " * size
    rows = [row for _ in range(size)]
    for r in rows:
        print(r)

if __name__ == '__main__':
    print_square_pattern(8)