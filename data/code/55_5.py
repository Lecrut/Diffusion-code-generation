def render_diamond_pattern(height):
    if height <= 0:
        return ""
    
    half_height = (height + 1) // 2
    lines = []
    
    for i in range(1, half_height + 1):
        spaces = ' ' * (half_height - i)
        chars = []
        for j in range(i):
            char_index = j + 65
            chars.append(chr(char_index))
        for j in range(i - 2, -1, -1):
            char_index = j + 65
            chars.append(chr(char_index))
        line = spaces + ''.join(chars) + spaces
        lines.append(line)
    
    for i in range(half_height - 1, 0, -1):
        spaces = ' ' * (half_height - i)
        chars = []
        for j in range(i):
            char_index = j + 65
            chars.append(chr(char_index))
        for j in range(i - 2, -1, -1):
            char_index = j + 65
            chars.append(chr(char_index))
        line = spaces + ''.join(chars) + spaces
        lines.append(line)
    
    return '\n'.join(lines)

if __name__ == '__main__':
    result = render_diamond_pattern(5)
    print(result)