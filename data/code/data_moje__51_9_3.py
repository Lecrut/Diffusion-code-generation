def build_symmetric_pyramid(rows):
    spacing_patterns = []
    for i in range(rows):
        spaces = ' ' * (rows - i - 1)
        numbers = ' '.join(str(digit + 1) for digit in range(i + 1))
        spacing_patterns.append(spaces + numbers + spaces)
    return '\n'.join(spacing_patterns)

if __name__ == '__main__':
    result = build_symmetric_pyramid(6)
    print(result)