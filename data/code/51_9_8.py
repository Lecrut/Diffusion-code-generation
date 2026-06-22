def build_symmetric_number_pyramid(rows):
    if rows <= 0:
        return []

    max_width = 2 * rows - 1
    pyramid = []

    for i in range(1, rows + 1):
        left_spaces = ' ' * (rows - i)

        if i == 1:
            line_str = str(1)
        else:
            increasing = [str(j) for j in range(1, i + 1)]
            decreasing = [str(j) for j in range(i - 1, 0, -1)]
            line_str = ''.join(increasing + decreasing)

        padded_line = left_spaces + line_str
        pyramid.append(padded_line)

    return pyramid

if __name__ == '__main__':
    pyramid = build_symmetric_number_pyramid(6)
    for line in pyramid:
        print(line)