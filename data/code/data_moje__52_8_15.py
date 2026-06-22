def render_diamond(height):
    lines = []
    mid = height // 2
    for i in range(height):
        if i <= mid:
            stars = 2 * i + 1
        else:
            stars = 2 * (height - i - 1) + 1
        spaces = (height - (stars // 2 + 1))
        line = ' ' * spaces + '*' * stars
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = render_diamond(7)
    print(result)