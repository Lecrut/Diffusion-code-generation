def render_diamond_pattern(height):
    if height <= 0:
        return ""
    upper_lines = []
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        left_part = ''.join(chr(ord('A') + j) for j in range(i))
        right_part = ''.join(chr(ord('A') + j) for j in range(i - 2, -1, -1))
        line = spaces + left_part + right_part
        upper_lines.append(line)
    lower_lines = []
    for i in range(height - 1, 0, -1):
        spaces = ' ' * (height - i)
        left_part = ''.join(chr(ord('A') + j) for j in range(i))
        right_part = ''.join(chr(ord('A') + j) for j in range(i - 2, -1, -1))
        line = spaces + left_part + right_part
        lower_lines.append(line)
    return '\n'.join(upper_lines + lower_lines)

if __name__ == '__main__':
    sample_height = 5
    result = render_diamond_pattern(sample_height)
    print(result)