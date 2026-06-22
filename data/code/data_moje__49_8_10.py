from math import ceil

def print_square_of_stars():
    SIZE = 9
    total_chars = SIZE * SIZE
    char_index = 0
    line_count = 0
    chars_in_line = 0
    while char_index < total_chars:
        print("*", end="")
        char_index += 1
        chars_in_line += 1
        if chars_in_line == SIZE:
            print()
            line_count += 1
            chars_in_line = 0
    return

if __name__ == '__main__':
    print_square_of_stars()