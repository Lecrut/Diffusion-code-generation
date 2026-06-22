def print_square_of_stars():
    i = 0
    while i < 9:
        j = 0
        row = ""
        while j < 9:
            row += "*"
            j += 1
        print(row)
        i += 1

if __name__ == '__main__':
    print_square_of_stars()