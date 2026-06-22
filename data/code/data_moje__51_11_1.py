def build_pyramid(height):
    lines = []
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        numbers = ' '.join(str((i - j) % (2 * i)) for j in range(i))
        line = f"{spaces}{numbers}{spaces}"
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(build_pyramid(7))