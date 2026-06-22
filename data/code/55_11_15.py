import string

def generate_alphabet_triangle(rows=5):
    alphabet = string.ascii_uppercase
    if rows > len(alphabet):
        rows = len(alphabet)
    lines = []
    current_chars = []
    for i in range(1, rows + 1):
        for j in range(i):
            if j < len(current_chars):
                current_chars.append(alphabet[j % len(alphabet)])
            else:
                char_index = len(current_chars) % len(alphabet)
                current_chars.append(alphabet[char_index])
        line = ' '.join(current_chars[:i])
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = generate_alphabet_triangle(5)
    print(result)