def generate_right_aligned_alphabet_triangle(height):
    if not isinstance(height, int) or height <= 0:
        return []
    result = []
    for row_index in range(1, height + 1):
        chars = [chr(ord('A') + i) for i in range(row_index)]
        row_string = ''.join(chars)
        padded_row = row_string.rjust(height + row_index - 1)
        result.append(padded_row)
    return result

if __name__ == '__main__':
    triangle_height = 5
    output_lines = generate_right_aligned_alphabet_triangle(triangle_height)
    for line in output_lines:
        print(line)