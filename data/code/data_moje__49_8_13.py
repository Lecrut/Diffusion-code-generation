def print_square_stars():
    size = 9
    row = 0
    while row < size:
        col = 0
        line = ""
        while col < size:
            line += "*"
            col += 1
        print(line)
        row += 1

if __name__ == "__main__":
    print_square_stars()