def render_diamond_pattern(height):
    if height <= 0:
        return ""
    lines = []
    upper = height - 1
    for i in range(height):
        spaces = ' ' * (upper - i)
        left_part = ''.join(chr(ord('A') + j) for j in range(i + 1))
        right_part = ''.join(chr(ord('A') + j) for j in range(i - 1, -1, -1))
        lines.append(spaces + left_part + right_part)
    lower = 1
    for i in range(height - 2, -1, -1):
        spaces = ' ' * (upper - i)
        left_part = ''.join(chr(ord('A') + j) for j in range(i + 1))
        right_part = ''.join(chr(ord('A') + j) for j in range(i - 1, -1, -1))
        lines.append(spaces + left_part + right_part)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(render_diamond_pattern(5))