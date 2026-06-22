def generate_alphabet_pyramid(rows):
    alphabet = [chr(code) for code in range(ord('A'), ord('Z') + 1)]
    pattern = []
    for i in range(rows):
        if i > len(alphabet):
            break
        row_chars = [alphabet[j % len(alphabet)] for j in range(i + 1)]
        row_str = ' '.join(row_chars)
        padding = ' ' * (rows - i - 1)
        pattern.append(padding + row_str)
    return pattern

if __name__ == '__main__':
    sample_rows = 5
    result = generate_alphabet_pyramid(sample_rows)
    for line in result:
        print(line)