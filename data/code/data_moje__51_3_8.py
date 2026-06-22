def generate_centered_number_pyramid(rows):
    if rows <= 0:
        return []
    max_num = rows
    max_width = len(str(max_num * 2 - 1)) + (rows - 1) * 2
    lines = []
    for i in range(1, rows + 1):
        nums = [str(n) for n in range(1, i + 1)] + [str(n) for n in range(i - 1, 0, -1)]
        line_content = " ".join(nums)
        line = line_content.center(max_width)
        lines.append(line)
    return lines

if __name__ == '__main__':
    result = generate_centered_number_pyramid(7)
    for line in result:
        print(line)