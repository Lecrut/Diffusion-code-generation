def generate_zigzag_triangle(rows):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    pattern = []
    current_char = 0
    direction = 1

    for row in range(1, rows + 1):
        row_chars = []
        for col in range(row):
            row_chars.append(alphabet[current_char % 26])
            current_char += direction
        pattern.append("".join(row_chars))
        if row == rows:
            break
        if current_char % 26 == 0 or current_char % 26 == 25:
            direction *= -1

    return "\n".join(pattern)

if __name__ == "__main__":
    result = generate_zigzag_triangle(5)
    print(result)