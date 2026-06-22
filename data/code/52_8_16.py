def render_diamond(height):
    if height % 2 == 0:
        height += 1
    mid = height // 2
    lines = []
    for i in range(mid + 1):
        spaces = mid - i
        stars = 2 * i + 1
        lines.append(' ' * spaces + '*' * stars)
    for i in range(mid - 1, -1, -1):
        spaces = mid - i
        stars = 2 * i + 1
        lines.append(' ' * spaces + '*' * stars)
    return lines

if __name__ == '__main__':
    result = render_diamond(7)
    for line in result:
        print(line)