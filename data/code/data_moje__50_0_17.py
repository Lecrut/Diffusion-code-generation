TRIANGLE_HEIGHT = 10
CHARACTER_STAR = "*"
CHARACTER_SPACE = " "

def print_right_aligned_triangle(rows: int) -> None:
    for current_row in range(1, rows + 1):
        padding_length = rows - current_row
        asterisk_count = current_row
        left_padding = CHARACTER_SPACE * padding_length
        current_line_asterisks = CHARACTER_STAR * asterisk_count
        print(left_padding + current_line_asterisks)

if __name__ == "__main__":
    print_right_aligned_triangle(TRIANGLE_HEIGHT)