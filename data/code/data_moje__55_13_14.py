def print_alphabet_triangle(num_rows=5):
    pattern_lines = []
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(num_rows):
        line = ''
        for j in range(i + 1):
            line += alphabet[j]
        pattern_lines.append(line)
    return '\n'.join(pattern_lines)
if __name__ == '__main__':
    result = print_alphabet_triangle(5)
    print(result)