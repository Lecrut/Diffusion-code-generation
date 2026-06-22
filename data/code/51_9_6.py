def build_symmetric_pyramid(rows: int) -> list[str]:
    if rows <= 0:
        return []
    
    padding_map = {}
    for r in range(1, rows + 1):
        padding_map[r] = rows - r
    
    pattern_cache = {}
    for r in range(1, rows + 1):
        center = r
        left_part = list(range(1, center + 1))
        right_part = list(range(center - 1, 0, -1)) if center > 1 else []
        full_row = left_part + right_part
        pattern_cache[r] = full_row
    
    result = []
    for r in range(1, rows + 1):
        padding = padding_map[r]
        row_numbers = pattern_cache[r]
        row_str = " ".join(str(num) for num in row_numbers)
        line = " " * padding + row_str + " " * padding
        result.append(line)
    
    return result

if __name__ == '__main__':
    sample_rows = 6
    pyramid_lines = build_symmetric_pyramid(sample_rows)
    for line in pyramid_lines:
        print(line)