def build_pyramid(height):
    lines = []
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        numbers = ' '.join(str(j % 10) for j in range(1, 2 * i))
        lines.append(f'{spaces}{numbers}')
    return '\n'.join(lines)

if __name__ == '__main__':
    print(build_pyramid(7))