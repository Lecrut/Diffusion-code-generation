def generate_alphabet_triangle(size):
    chars = [chr(ord('A') + i) for i in range(26)]
    rows = []
    for i in range(size):
        row_chars = [chars[j % 26] for j in range(i + 1)]
        rows.append(" ".join(row_chars))
    return "\n".join(rows)

if __name__ == '__main__':
    result = generate_alphabet_triangle(5)
    print(result)