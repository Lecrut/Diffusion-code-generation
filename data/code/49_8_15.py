def print_square_of_stars():
    SIZE = 9
    if not isinstance(SIZE, int) or SIZE <= 0:
        raise ValueError("Size must be a positive integer")
    
    row_count = 0
    while row_count < SIZE:
        col_count = 0
        current_line = []
        while col_count < SIZE:
            current_line.append("*")
            col_count += 1
        print("".join(current_line))
        row_count += 1

if __name__ == '__main__':
    print_square_of_stars()