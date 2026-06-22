def build_pyramid():
    levels = 4
    max_width = 2 * levels - 1
    pyramid_lines = []
    for level in range(1, levels + 1):
        row_numbers = [str(i) for i in range(1, level + 1)]
        row_string = ' '.join(row_numbers)
        padding = (max_width - len(row_string.replace(' ', ''))) // 2
        padded_row = row_string.rjust(max_width).ljust(max_width)
        pyramid_lines.append(padded_row)
    return '\n'.join(pyramid_lines)

if __name__ == '__main__':
    result = build_pyramid()
    print(result)