def render_diamond_pattern(height: int) -> list[str]:
    if height <= 0:
        return []
    
    if height == 1:
        return ["A"]
    
    mid_index = height - 1
    result = []
    
    for i in range(mid_index):
        char_code = ord('A') + i
        char = chr(char_code)
        side_spaces = mid_index - i
        if i == 0:
            line = " " * side_spaces + char + " " * side_spaces
        else:
            inner_spaces = 2 * i - 1
            line = " " * side_spaces + char + " " * inner_spaces + char + " " * side_spaces
        result.append(line)
    
    mid_char_code = ord('A') + mid_index
    mid_char = chr(mid_char_code)
    result.append(mid_char)
    
    for i in reversed(range(mid_index)):
        char_code = ord('A') + i
        char = chr(char_code)
        side_spaces = mid_index - i
        if i == 0:
            line = " " * side_spaces + char + " " * side_spaces
        else:
            inner_spaces = 2 * i - 1
            line = " " * side_spaces + char + " " * inner_spaces + char + " " * side_spaces
        result.append(line)
    
    return result

if __name__ == '__main__':
    sample_height = 4
    pattern = render_diamond_pattern(sample_height)
    for line in pattern:
        print(line)