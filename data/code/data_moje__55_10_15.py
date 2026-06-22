def print_alphabet_triangle(height):
    result = []
    for i in range(1, height + 1):
        row_chars = []
        for j in range(i):
            char = chr(ord('A') + j)
            row_chars.append(char)
        result.append(" ".join(row_chars))
    return "\n".join(result)

if __name__ == '__main__':
    h = 5
    output = print_alphabet_triangle(h)
    print(output)