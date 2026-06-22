def render_diamond_pattern(height):
    if height < 1:
        return []
    chars = [chr(ord('A') + i) for i in range(height)]
    lines = []
    for i in range(height):
        spaces = ' ' * (height - 1 - i)
        line_parts = []
        for k in range(i + 1):
            line_parts.append(chars[k])
            if k < i:
                line_parts.append(' ')
        if i == 0:
            line = spaces + chars[0]
        else:
            line = spaces + ''.join(line_parts)
        lines.append(line)
    for i in range(height - 2, -1, -1):
        spaces = ' ' * (height - 1 - i)
        line_parts = []
        for k in range(i + 1):
            line_parts.append(chars[k])
            if k < i:
                line_parts.append(' ')
        if i == 0:
            line = spaces + chars[0]
        else:
            line = spaces + ''.join(line_parts)
        lines.append(line)
    return lines

if __name__ == '__main__':
    sample_height = 4
    result = render_diamond_pattern(sample_height)
    for line in result:
        print(line)