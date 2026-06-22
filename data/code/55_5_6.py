def render_diamond(height):
    if height <= 0:
        return ""
    if height % 2 == 0:
        height += 1
    mid = height // 2
    lines = []
    for i in range(height):
        dist = abs(i - mid)
        num_spaces = dist
        num_stars = height - 2 * dist
        line = ' ' * num_spaces + '*' * num_stars
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(render_diamond(7))