def print_star_square():
    side_length = 5
    pattern = "*\n" * side_length
    line = "* " * (side_length - 1) + "*"
    rows = [line] * side_length
    print("\n".join(rows))

if __name__ == '__main__':
    print_star_square()