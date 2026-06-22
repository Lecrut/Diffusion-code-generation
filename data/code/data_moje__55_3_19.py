def inverted_alphabet_triangle(n):
    lines = []
    for i in range(n):
        row_chars = [chr(ord('A') + i)] * (n - i)
        lines.append("".join(row_chars))
    return "\n".join(lines)

if __name__ == '__main__':
    print(inverted_alphabet_triangle(5))