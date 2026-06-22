def build_symmetric_pyramid(rows):
    if rows <= 0:
        return []
    
    pre_calculated_spaces = []
    for i in range(rows):
        pre_calculated_spaces.append(' ' * (rows - 1 - i))
    
    pyramid = []
    for i in range(rows):
        left_side = ''.join(str(j) for j in range(1, i + 2))
        right_side = ''.join(str(j) for j in range(i, 0, -1))
        full_line = pre_calculated_spaces[i] + left_side + right_side
        pyramid.append(full_line)
    
    return pyramid

if __name__ == '__main__':
    sample_rows = 6
    result = build_symmetric_pyramid(sample_rows)
    for line in result:
        print(line)