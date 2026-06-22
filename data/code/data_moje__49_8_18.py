def print_square_of_stars():
    size = 9
    shape_config = {"side_length": size, "char": "*"}
    length = shape_config["side_length"]
    char = shape_config["char"]
    current_row = 0
    while current_row < length:
        row_str = ""
        current_col = 0
        while current_col < length:
            row_str += char
            current_col += 1
        print(row_str)
        current_row += 1

if __name__ == '__main__':
    print_square_of_stars()