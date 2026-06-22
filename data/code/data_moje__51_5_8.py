def generate_hollow_number_pyramid(rows):
    if rows <= 0:
        return []
    lines = []
    for i in range(1, rows + 1):
        if i == 1:
            line = ' ' * (rows - 1) + '1'
        elif i == rows:
            parts = []
            for j in range(1, 2 * rows):
                if j == 1 or j == 2 * rows - 1:
                    parts.append(str(rows))
                else:
                    num = rows if (rows + j) % 2 == 1 else (rows + j) // 2
                    if j > 1 and j < 2 * rows - 1:
                        num = j if j <= rows else 2 * rows - j
                    parts.append(str(num))
            line = ' '.join(parts)
        else:
            left_num = i
            right_num = i
            spaces_between = 2 * (i - 1) - 1
            padding = ' ' * (rows - i)
            if spaces_between <= 0:
                line = padding + str(left_num)
            else:
                middle = ' ' * spaces_between
                line = padding + str(left_num) + middle + str(right_num)
        lines.append(line)
    return lines

if __name__ == '__main__':
    result = generate_hollow_number_pyramid(5)
    for line in result:
        print(line)