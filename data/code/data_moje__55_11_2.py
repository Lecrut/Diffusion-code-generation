def generate_alphabet_triangle(rows):
    result = []
    current_row = []
    for i in range(1, rows + 1):
        char_code = ord('A') + i - 1
        current_row.append(chr(char_code))
        row_str = ''.join(current_row)
        result.append(row_str)
    return result
if __name__ == '__main__':
    rows = 5
    triangle = generate_alphabet_triangle(rows)
    for line in triangle:
        print(line)