def generate_right_aligned_alphabet_triangle(rows):
    triangle = []
    for i in range(1, rows + 1):
        spaces = ' ' * (rows - i)
        letters = ''.join(chr(ord('A') + j) for j in range(i))
        triangle.append(spaces + letters)
    return triangle

if __name__ == '__main__':
    sample_rows = 5
    result = generate_right_aligned_alphabet_triangle(sample_rows)
    for line in result:
        print(line)