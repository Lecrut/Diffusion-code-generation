def render_diamond_alphabet_pattern(height):
    if height < 1:
        return ""
    
    letters = [chr(ord('A') + i) for i in range(height)]
    lines = []
    
    for i in range(height):
        spaces = ' ' * (height - 1 - i)
        left_part = ''.join(letters[j] for j in range(i + 1))
        right_part = ''.join(letters[j] for j in range(i - 1, -1, -1))
        line = spaces + left_part + right_part
        lines.append(line)
    
    for i in range(height - 2, -1, -1):
        spaces = ' ' * (height - 1 - i)
        left_part = ''.join(letters[j] for j in range(i + 1))
        right_part = ''.join(letters[j] for j in range(i - 1, -1, -1))
        line = spaces + left_part + right_part
        lines.append(line)
    
    return '\n'.join(lines)

if __name__ == '__main__':
    result = render_diamond_alphabet_pattern(5)
    print(result)