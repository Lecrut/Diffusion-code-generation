def render_diamond_alphabet(height: int) -> str:
    if height <= 0:
        return ""
    
    middle = height // 2 + 1
    lines = []
    
    for i in range(1, middle + 1):
        spaces = " " * (middle - i)
        char_code = 64 + i
        char = chr(char_code)
        if i == 1:
            line = spaces + char
        else:
            middle_chars = " " * (2 * i - 3)
            line = spaces + char + middle_chars + char + spaces
        lines.append(line)
        
    for i in range(middle - 1, 0, -1):
        spaces = " " * (middle - i)
        char_code = 64 + i
        char = chr(char_code)
        if i == 1:
            line = spaces + char
        else:
            middle_chars = " " * (2 * i - 3)
            line = spaces + char + middle_chars + char + spaces
        lines.append(line)
        
    return "\n".join(lines)

if __name__ == '__main__':
    result = render_diamond_alphabet(5)
    print(result)