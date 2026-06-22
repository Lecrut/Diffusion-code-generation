import string

def print_centered_alphabet_triangle(height):
    if height <= 0:
        return
    letters = list(string.ascii_uppercase)
    max_chars = 2 * height - 1
    for i in range(height):
        row_chars = letters[:i + 1]
        left_part = row_chars[:-1][::-1]
        center_part = row_chars[-1]
        full_row = left_part + [center_part] + left_part
        row_str = "".join(full_row)
        padding = (max_chars - len(row_str)) // 2
        print(" " * padding + row_str)

if __name__ == "__main__":
    sample_height = 5
    print_centered_alphabet_triangle(sample_height)