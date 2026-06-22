def render_diamond(height):
    if height <= 0:
        return []
    
    mid = (height + 1) // 2
    result = []
    
    for i in range(1, mid + 1):
        char_code = ord('A') + i - 1
        char = chr(char_code)
        outer_spaces = ' ' * (mid - i)
        inner_spaces = ' ' * (2 * i - 3) if i > 1 else ''
        
        if i == 1:
            row = outer_spaces + char + outer_spaces
        else:
            row = outer_spaces + char + inner_spaces + char + outer_spaces
        result.append(row)
    
    for i in range(mid - 1, 0, -1):
        char_code = ord('A') + i - 1
        char = chr(char_code)
        outer_spaces = ' ' * (mid - i)
        inner_spaces = ' ' * (2 * i - 3) if i > 1 else ''
        
        if i == 1:
            row = outer_spaces + char + outer_spaces
        else:
            row = outer_spaces + char + inner_spaces + char + outer_spaces
        result.append(row)
        
    return result

if __name__ == '__main__':
    lines = render_diamond(5)
    for line in lines:
        print(line)