def build_centered_pyramid(height):
    lines = []
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        numbers = ' '.join(str((j % 9) + 1) for j in range(2 * i - 1))
        lines.append(f'{spaces}{numbers}')
    return '\n'.join(lines)

if __name__ == '__main__':
    pyramid = build_centered_pyramid(7)
    print(pyramid)