def render_pyramid(rows):
    result_lines = []
    max_width = rows * 2 - 1
    for i in range(1, rows + 1):
        num = i
        left_part = str(num)
        for _ in range(i - 2, -1, -1):
            left_part = str(num - 1) + left_part
        right_part = left_part[::-1]
        full_line = left_part + right_part[1:]
        centered_line = full_line.center(max_width)
        result_lines.append(centered_line)
    return "\n".join(result_lines)

if __name__ == '__main__':
    ROWS = 8
    print(render_pyramid(ROWS))