def generate_pyramid(height):
    lines = []
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        numbers = ' '.join(str((i - 1) % 10 + 1) for _ in range(i))
        lines.append(f'{spaces}{numbers}')
    return '\n'.join(lines)

if __name__ == '__main__':
    print(generate_pyramid(7))