def print_square_of_stars():
    i = 0
    size = 9
    while i < size:
        j = 0
        row = ''
        while j < size:
            row += '*'
            j += 1
        print(row)
        i += 1

if __name__ == '__main__':
    result = print_square_of_stars()