def inverted_alphabet_triangle(rows=5):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result_lines = []
    for i in range(rows, 0, -1):
        line = alphabet[:i]
        result_lines.append(line)
    return "\n".join(result_lines)

if __name__ == '__main__':
    print(inverted_alphabet_triangle(5))