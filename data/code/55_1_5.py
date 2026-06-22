def print_centered_alphabet_triangle(height):
    lines = []
    for i in range(1, height + 1):
        chars = [chr(ord('A') + j) for j in range(i)]
        row_content = ' '.join(chars)
        max_width = 2 * height - 1
        current_width = len(row_content)
        padding = (max_width - current_width) // 2
        line = ' ' * padding + row_content
        lines.append(line)
    return '\n'.join(lines)
if __name__ == '__main__':
    height = 5
    result = print_centered_alphabet_triangle(height)
    print(result)