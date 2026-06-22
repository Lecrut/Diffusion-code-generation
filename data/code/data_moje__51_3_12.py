def generate_centered_number_pyramid(rows: int) -> list[str]:
    center_col = rows - 1
    lines = []
    for row in range(1, rows + 1):
        num = row
        line_nums = [str(num) for _ in range(row)]
        line_str = " ".join(line_nums)
        padding = " " * (center_col * 2 - len(line_str) // 2)
        if row < rows:
            padding = padding[:len(line_str)//2]
        else:
            padding = padding
        total_width = (rows * 2 - 1) * 2
        centered_line = line_str.center(total_width)
        lines.append(centered_line)
    return lines

if __name__ == '__main__':
    result = generate_centered_number_pyramid(7)
    for line in result:
        print(line)