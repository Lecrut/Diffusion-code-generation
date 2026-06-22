def generate_zigzag_triangle(rows):
    if rows < 1:
        return []
    result = []
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    current_index = 0
    for r in range(1, rows + 1):
        line_chars = []
        for _ in range(r):
            line_chars.append(alphabet[current_index % 26])
            current_index += 1
        result.append("".join(line_chars))
    return result

if __name__ == "__main__":
    sample_rows = 6
    output = generate_zigzag_triangle(sample_rows)
    for line in output:
        print(line)