def generate_zigzag_triangle(rows):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    for i in range(1, rows + 1):
        line_chars = []
        for j in range(i):
            idx = (i + j) % 26
            line_chars.append(alphabet[idx])
        result.append("".join(line_chars))
    return "\n".join(result)

if __name__ == "__main__":
    print(generate_zigzag_triangle(5))