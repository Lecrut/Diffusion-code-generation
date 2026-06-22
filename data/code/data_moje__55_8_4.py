def zigzag_alphabet_triangle(rows):
    if rows <= 0:
        return ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result_lines = []
    for i in range(1, rows + 1):
        chars = []
        for j in range(i):
            index = j if j < len(alphabet) else (j % 26)
            if index < len(alphabet):
                chars.append(alphabet[index])
            else:
                chars.append(alphabet[index % 26])
        result_lines.append("".join(chars))
    return "\n".join(result_lines)

if __name__ == '__main__':
    print(zigzag_alphabet_triangle(5))