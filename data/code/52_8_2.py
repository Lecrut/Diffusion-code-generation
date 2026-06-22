def render_diamond(height):
    rows = []
    for i in range(height):
        spaces = abs(height // 2 - i)
        stars = height - 2 * spaces
        row = ' ' * spaces + '* ' * stars
        rows.append(row.rstrip())
    return '\n'.join(rows)

if __name__ == '__main__':
    print(render_diamond(7))