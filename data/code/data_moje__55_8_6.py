import string

def zigzag_alphabet_triangle(rows: int) -> str:
    alphabet = string.ascii_uppercase
    pattern = []
    for i in range(1, rows + 1):
        line = []
        for j in range(1, i + 1):
            char_index = (j - 1) % 26
            if (j - 1) // 26 % 2 == 0:
                line.append(alphabet[char_index])
            else:
                line.append(alphabet[char_index])
        pattern.append(' '.join(line))
    return '\n'.join(pattern)

if __name__ == '__main__':
    result = zigzag_alphabet_triangle(5)
    print(result)