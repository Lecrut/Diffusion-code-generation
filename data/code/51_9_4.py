def build_symmetric_pyramid(rows: int) -> list:
    pattern_cache = {}
    
    def get_spacing_pattern(row_index: int, total_rows: int) -> str:
        if row_index in pattern_cache:
            return pattern_cache[row_index]
        
        max_width = total_rows - 1
        current_spacing = max_width - row_index
        
        left_spaces = ' ' * current_spacing
        middle_numbers = list(range(1, row_index + 1))
        right_numbers = list(range(row_index, 0, -1))
        
        combined_numbers = middle_numbers + right_numbers
        
        if row_index == 0:
            line = left_spaces + '1'
        else:
            line = left_spaces + ' '.join(str(n) for n in combined_numbers)
            
        pattern_cache[row_index] = line
        return line

    pyramid_lines = []
    for r in range(rows):
        line = get_spacing_pattern(r, rows)
        pyramid_lines.append(line)
        
    return pyramid_lines

if __name__ == '__main__':
    sample_rows = 6
    result = build_symmetric_pyramid(sample_rows)
    for line in result:
        print(line)