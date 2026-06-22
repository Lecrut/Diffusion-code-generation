def build_symmetric_number_pyramid(rows):
    if rows <= 0:
        return []
    pre_calculated_spacing = {}
    for r in range(1, rows + 1):
        spaces = rows - r
        pre_calculated_spacing[r] = ' ' * spaces
    result = []
    for r in range(1, rows + 1):
        leading_spaces = pre_calculated_spacing[r]
        numbers = list(range(1, r + 1)) + list(range(r - 1, 0, -1))
        line = leading_spaces + ' '.join(map(str, numbers)) + leading_spaces
        result.append(line)
    return result

if __name__ == '__main__':
    pyramid = build_symmetric_number_pyramid(6)
    for line in pyramid:
        print(line)