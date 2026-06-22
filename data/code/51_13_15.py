def generate_pyramid(rows=8):
    pyramid_lines = []
    for i in range(1, rows + 1):
        spaces = ' ' * (rows - i)
        numbers = ' '.join(str(j % 10) for j in range(1, 2 * i))
        pyramid_lines.append(spaces + numbers)
    return '\n'.join(pyramid_lines)

if __name__ == '__main__':
    print(generate_pyramid())