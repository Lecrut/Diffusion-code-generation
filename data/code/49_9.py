def print_square_stars(size=12):
    row = "* " * size
    rows = [row.strip()] * size
    result = "\n".join(rows)
    return result

if __name__ == '__main__':
    print(print_square_stars(12))