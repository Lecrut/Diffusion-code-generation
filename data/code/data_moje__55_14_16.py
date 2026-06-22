def generate_centered_alphabet_triangle(height):
    result = []
    for i in range(1, height + 1):
        chars = [chr(ord('A') + j) for j in range(i)]
        center_line = ''.join(chars)
        total_width = 2 * height - 1
        padding = (total_width - len(center_line)) // 2
        line = ' ' * padding + center_line + ' ' * padding
        result.append(line)
    return result

if __name__ == '__main__':
    sample_height = 5
    triangle_lines = generate_centered_alphabet_triangle(sample_height)
    print(triangle_lines)