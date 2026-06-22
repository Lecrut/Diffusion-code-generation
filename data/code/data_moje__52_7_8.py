def generate_diamond(n):
    lines = []
    for i in range(1, 2 * n):
        stars = 2 * min(i, 2 * n - i) - 1
        spaces = n - min(i, 2 * n - i)
        lines.append(' ' * spaces + '* ' * (stars // 2 + (1 if stars % 2 else 0))[:-1].replace('*', ' *').strip().replace('*', '*', 0))
        line_stars = '* ' * stars
        line_stars = line_stars.rstrip()
        line_spaces = ' ' * (n - min(i, 2 * n - i))
        lines.append(line_spaces + line_stars)
    return '\n'.join(lines)

def get_diamond_string(size):
    rows = []
    for i in range(size * 2):
        dist_top = i
        dist_bottom = size * 2 - 2 - i
        current_width = size * 2 - 1 - 2 * max(dist_top, dist_bottom)
        if current_width > 0:
            stars = '* ' * (current_width // 2 + 1)
            row_str = stars.rstrip()
            indent = ' ' * ((size * 2 - 1 - current_width) // 2)
            rows.append(indent + row_str)
    return '\n'.join(rows)
if __name__ == '__main__':
    size = 5
    result = get_diamond_string(size)
    print(result)