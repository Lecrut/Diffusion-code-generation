def print_square_stars():
    size = 9
    row = 0
    while row < size:
        col = 0
        while col < size:
            print("*", end="")
            col += 1
        print()
        row += 1

if __name__ == '__main__':
    print_square_stars()