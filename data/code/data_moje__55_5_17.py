def render_diamond_pattern(height):
    if height <= 0:
        return []
    
    pattern = []
    mid = height // 2
    
    for i in range(mid + 1):
        space_count = mid - i
        char_index = i
        char = chr(ord('A') + char_index)
        
        row = ' ' * space_count + char
        if i > 0:
            inner_spaces = 2 * i - 1
            row += ' ' * inner_spaces + char
        pattern.append(row)
        
        if i < mid:
            reverse_index = mid - i - 1
            reverse_space_count = i + 1
            reverse_char_index = reverse_index
            reverse_char = chr(ord('A') + reverse_char_index)
            
            reverse_row = ' ' * reverse_space_count + reverse_char
            if reverse_index > 0:
                reverse_inner_spaces = 2 * reverse_index - 1
                reverse_row += ' ' * reverse_inner_spaces + reverse_char
            pattern.append(reverse_row)
            
    return pattern

if __name__ == '__main__':
    sample_height = 5
    result = render_diamond_pattern(sample_height)
    for line in result:
        print(line)