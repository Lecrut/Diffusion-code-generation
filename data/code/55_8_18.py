def zigzag_triangle(rows):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    lines = []
    for row in range(rows):
        current_char = alphabet[row % len(alphabet)]
        space_count = row
        line = " " * space_count + current_char
        lines.append(line)
    for row in range(rows - 2, -1, -1):
        current_char = alphabet[row % len(alphabet)]
        space_count = row
        line = " " * space_count + current_char
        lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    sample_rows = 5
    result = zigzag_triangle(sample_rows)
    print(result)