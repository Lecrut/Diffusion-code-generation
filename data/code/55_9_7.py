def generate_mirrored_alphabet_triangle(size):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if size > 26:
        size = 26
    result = []
    for i in range(size):
        row_chars = [alphabet[j] for j in range(i + 1)]
        left_part = ''.join(row_chars)
        right_part = ''.join(row_chars[-2::-1]) if i > 0 else ''
        row = left_part + right_part
        result.append(row)
    return result

if __name__ == '__main__':
    size = 5
    output = generate_mirrored_alphabet_triangle(size)
    for line in output:
        print(line)