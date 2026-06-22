def render_diamond_pattern(height):
    if height <= 0 or height % 2 == 0:
        raise ValueError("Height must be a positive odd integer")
    
    mid = height // 2
    result_lines = []
    
    for i in range(height):
        if i <= mid:
            row_idx = i
        else:
            row_idx = height - 1 - i
        
        spaces = ' ' * (mid - row_idx)
        left_chars = []
        for j in range(row_idx + 1):
            char_code = ord('A') + j
            left_chars.append(chr(char_code))
        right_chars = left_chars[-2::-1] if row_idx > 0 else []
        middle_part = ''.join(left_chars) + ''.join(right_chars)
        result_lines.append(spaces + middle_part + spaces)
    
    return '\n'.join(result_lines)

if __name__ == '__main__':
    pattern = render_diamond_pattern(5)
    print(pattern)