def generate_centered_alphabet_triangle(size: int) -> list[str]:
    if size < 1:
        return []

    letters = [chr(ord('A') + i) for i in range(size)]
    result = []
    max_width = (size * 2) - 1

    for i in range(size):
        current_letters = letters[:i + 1]
        row_str = ''.join(current_letters)
        spacing_needed = (max_width - len(row_str)) // 2
        full_row = ' ' * spacing_needed + row_str
        result.append(full_row)

    return result

if __name__ == '__main__':
    triangle_lines = generate_centered_alphabet_triangle(5)
    for line in triangle_lines:
        print(line)