def generate_diamond(height):
    lines = []
    half = height // 2
    for i in range(height):
        if i <= half:
            spaces = half - i
            stars = 2 * i + 1
        else:
            spaces = i - half
            stars = 2 * (height - i) - 1
        line = ' ' * spaces + '*' * stars
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = generate_diamond(7)
    print(result)