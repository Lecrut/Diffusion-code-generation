def generate_alphabet_triangle(size):
    if size <= 0:
        return ""
    import string
    alphabet = string.ascii_uppercase
    lines = []
    for i in range(1, size + 1):
        chars = alphabet[:i]
        line = " ".join(chars)
        lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    result = generate_alphabet_triangle(5)
    print(result)