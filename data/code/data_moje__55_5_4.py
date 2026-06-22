def render_diamond_pattern(height):
    if height < 1:
        return ""
    mid = (height + 1) // 2
    lines = []
    upper_chars = [chr(ord('A') + i) for i in range(mid)]
    lower_chars = upper_chars[:-1][::-1]
    for i in range(mid):
        char = upper_chars[i]
        spaces = ' ' * (mid - 1 - i)
        left_part = ''.join(upper_chars[:i + 1][::-1])
        right_part = ''.join(upper_chars[1:i + 1])
        line = spaces + left_part + right_part
        lines.append(line)
    for i in range(mid - 1, -1, -1):
        char = upper_chars[i]
        spaces = ' ' * (mid - 1 - i)
        left_part = ''.join(upper_chars[:i + 1][::-1])
        right_part = ''.join(upper_chars[1:i + 1])
        line = spaces + left_part + right_part
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = render_diamond_pattern(5)
    print(result)