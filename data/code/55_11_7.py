def generate_alphabet_triangle(rows=5):
    if rows <= 0:
        return []
    result = []
    current_chars = []
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    char_index = 0
    for i in range(1, rows + 1):
        for _ in range(i):
            if char_index < len(alphabet):
                current_chars.append(alphabet[char_index])
                char_index += 1
            else:
                current_chars.append('?')
        result.append(''.join(current_chars))
        current_chars = []
    return result

if __name__ == '__main__':
    triangle = generate_alphabet_triangle(5)
    for line in triangle:
        print(line)