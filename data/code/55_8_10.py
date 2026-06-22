def generate_zigzag_triangle(rows):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    direction = 1
    index = 0
    for row in range(1, rows + 1):
        line_chars = []
        for col in range(row):
            line_chars.append(alphabet[index % len(alphabet)])
            index += 1
        if row % 2 == 0:
            line_chars.reverse()
        result.append("".join(line_chars))
    return result

if __name__ == '__main__':
    sample_rows = 7
    print(generate_zigzag_triangle(sample_rows))