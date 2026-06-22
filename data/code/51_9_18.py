def build_symmetric_pyramid(rows: int) -> list:
    precalculated_spaces = {}
    for i in range(rows):
        precalculated_spaces[i] = rows - i - 1
    
    result = []
    for i in range(rows):
        spaces = precalculated_spaces[i]
        left_side = list(range(1, i + 2))
        right_side = list(range(i, 0, -1))
        full_row = left_side + right_side
        line_str = ' ' * spaces + ' '.join(map(str, full_row))
        result.append(line_str)
    return result

if __name__ == '__main__':
    sample_rows = 6
    pyramid_output = build_symmetric_pyramid(sample_rows)
    for line in pyramid_output:
        print(line)