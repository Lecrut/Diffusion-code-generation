def hollow_number_pyramid(rows: int) -> str:
    if rows <= 0:
        return ''
    if rows == 1:
        return '1\n'
    result = []
    result.append(str(1))
    for i in range(2, rows):
        spaces = ' ' * (rows - i)
        left_part = str(i)
        middle_spaces = ' ' * ((i - 2) * 2 + 1) if i > 2 else ''
        right_part = str(i)
        line = spaces + left_part + middle_spaces + right_part
        result.append(line)
    last_row_width = (rows - 1) * 2 + 1
    last_line = ' ' * (rows - rows) + str(rows)
    result.clear()
    for i in range(1, rows + 1):
        if i == 1:
            line = ' ' * (rows - 1) + '1'
            result.append(line)
        elif i == rows:
            line = ' ' * (rows - rows) + str(rows)
            result.append(line)
        else:
            spaces_before = ' ' * (rows - i)
            left_num = str(i)
            right_num = str(i)
            gap_width = (i - 1) * 2 - 1
            if gap_width < 1:
                gap_width = 1
            part1 = ' ' * (rows - i)
            part2 = str(i)
            if i > 1:
                gap = ' ' * ((i - 2) * 2 + 1)
                part3 = str(i)
                line = part1 + part2 + gap + part3
            else:
                line = part1 + part2
            result.append(line)
    return '\n'.join(result) + '\n'
if __name__ == '__main__':
    output = hollow_number_pyramid(5)
    print(output)