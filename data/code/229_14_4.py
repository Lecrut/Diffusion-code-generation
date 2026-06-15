def print_square_grid(size):
    for i in range(size):
        row = ""
        for j in range(size):
            if i == j:
                row += "* "
            else:
                row += "  "
        print(row)
if __name__ == '__main__':
    dimensions = "5"
    try:
        size = int(dimensions)
        print_square_grid(size)
    except ValueError:
        pass