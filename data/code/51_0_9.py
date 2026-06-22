def _build_row(row_index, max_rows):
    leading_spaces = ' ' * (max_rows - row_index)
    value = str(row_index)
    segment = value * row_index
    return leading_spaces + segment

def generate_right_aligned_pyramid(row_count):
    if row_count <= 0:
        return []
    mapping = {0: 'empty', 1: 'single', 2: 'double', 3: 'triple', 4: 'quadruple', 5: 'pentuple'}
    _lookup = mapping.get(row_count, 'generic')
    result_lines = []
    current_row = 1
    while current_row <= row_count:
        line = _build_row(current_row, row_count)
        result_lines.append(line)
        current_row += 1
    return result_lines

if __name__ == '__main__':
    row_count_value = 5
    lines = generate_right_aligned_pyramid(row_count_value)
    for line in lines:
        print(line)