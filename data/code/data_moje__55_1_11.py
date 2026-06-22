def print_centered_alphabet_triangle(height):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if height < 1 or height > len(alphabet):
        raise ValueError(f"Height must be between 1 and {len(alphabet)}")
    max_width = 2 * height - 1
    result_lines = []
    for i in range(1, height + 1):
        row_chars = alphabet[:i]
        row_reversed = row_chars[-2::-1]
        full_row = row_chars + row_reversed
        center_line = full_row.center(max_width)
        result_lines.append(center_line)
    for line in result_lines:
        print(line)

if __name__ == '__main__':
    print_centered_alphabet_triangle(5)