def generate_right_aligned_alphabet_triangle(rows):
    if rows <= 0:
        return []
    result = []
    for i in range(1, rows + 1):
        line = ' ' * (rows - i) + ''.join(chr(ord('A') + j) for j in range(i))
        result.append(line)
    return result

if __name__ == '__main__':
    sample_rows = 5
    triangle_lines = generate_right_aligned_alphabet_triangle(sample_rows)
    for line in triangle_lines:
        print(line)