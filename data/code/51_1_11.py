def create_symmetric_pyramid(levels):
    if levels < 1:
        return ''
    base_width = 2 * levels - 1
    pyramid_lines = []
    for level in range(1, levels + 1):
        number = level
        left_part = ''.join((str(i) for i in range(1, level)))
        right_part = ''.join((str(level - i) for i in range(1, level)))[::-1]
        center = str(number)
        line_content = left_part + center + right_part
        padding = (base_width - len(line_content)) // 2
        full_line = ' ' * padding + line_content + ' ' * padding
        pyramid_lines.append(full_line.rstrip())
    return '\n'.join(pyramid_lines)
if __name__ == '__main__':
    num_levels = 4
    pyramid_output = create_symmetric_pyramid(num_levels)
    print(pyramid_output)