def print_centered_alphabet_triangle(height):
    if height <= 0:
        return
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if height > 26:
        height = 26
    max_width = 2 * height - 1
    for i in range(1, height + 1):
        row_chars = alphabet[:i]
        row = "".join(row_chars[i-j] for j in range(i-1, -1, -1))
        row = "".join(row)
        print(row.center(max_width))

if __name__ == "__main__":
    print_centered_alphabet_triangle(7)