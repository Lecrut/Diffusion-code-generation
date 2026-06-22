import string

def print_alphabet_triangle(height):
    alphabet = string.ascii_uppercase
    lines = []
    for i in range(1, height + 1):
        chars = list(alphabet[i - 1])
        for j in range(2, i + 1):
            chars.append(alphabet[(i - j) % len(alphabet)])
        line = ''.join(reversed(chars))
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = print_alphabet_triangle(5)
    print(result)