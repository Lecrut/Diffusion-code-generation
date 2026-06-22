def inverted_alphabet_triangle(n):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lines = []
    for i in range(n, 0, -1):
        line = alphabet[:i]
        lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    result = inverted_alphabet_triangle(5)
    print(result)