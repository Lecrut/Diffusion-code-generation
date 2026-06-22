def generate_centered_alphabet_triangle(height):
    if height <= 0:
        return []

    triangle = []
    for i in range(height):
        chars = ''.join(
            chr(ord('A') + j)
            for j in range(i + 1)
        )
        spaces = ' ' * (height - i - 1)
        triangle.append(spaces + chars + spaces)

    return triangle

if __name__ == '__main__':
    print(generate_centered_alphabet_triangle(5))