def generate_hollow_alphabet_triangle(width):
    if width < 1:
        return []
    rows = []
    for i in range(1, width + 1):
        if i == 1:
            rows.append(['A'])
        else:
            row = [''] * (2 * i - 1)
            row[0] = chr(ord('A') + i - 1)
            row[-1] = chr(ord('A') + i - 1)
            middle_chars = []
            for j in range(1, i):
                middle_chars.append(' ')
            for k in range(1, i):
                row[k] = ' '
                row[-(k + 1)] = ' '
            rows.append(row)
    result = []
    max_width = 2 * width - 1
    for row_chars in rows:
        s = ''.join(row_chars)
        padded = s.center(max_width)
        result.append(padded)
    return result

def print_pattern():
    width = 5
    pattern = generate_hollow_alphabet_triangle(width)
    for line in pattern:
        print(line)
if __name__ == '__main__':
    print_pattern()