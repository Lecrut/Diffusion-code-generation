def print_square(size):
    rows = 0
    while rows < size:
        cols = 0
        row_str = ""
        while cols < size:
            row_str += "*"
            cols += 1
        print(row_str)
        rows += 1

if __name__ == '__main__':
    print_square(5)