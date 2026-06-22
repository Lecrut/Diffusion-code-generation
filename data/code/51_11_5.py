def build_number_pyramid(height):
    lines = []
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        numbers = ' '.join(str(x) for x in range(1, i + 1)) + ' ' + ' '.join(str(x) for x in range(i - 1, 0, -1))
        lines.append(f"{spaces}{numbers}")
    return '\n'.join(lines)

if __name__ == '__main__':
    result = build_number_pyramid(7)
    print(result)