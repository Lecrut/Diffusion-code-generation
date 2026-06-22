def generate_centered_alphabet_triangle(n_rows=None):
    if n_rows is None:
        n_rows = 5

    lines = []
    for i in range(1, n_rows + 1):
        row_str = ""
        for j in range(1, i * 2):
            if j <= i:
                char_index = j - 1
            else:
                char_index = i * 2 - j - 1
            row_str += chr(ord('A') + char_index)
        padded_line = row_str.center(n_rows * 2 - 1)
        lines.append(padded_line)

    return lines

if __name__ == '__main__':
    result = generate_centered_alphabet_triangle()
    for line in result:
        print(line)