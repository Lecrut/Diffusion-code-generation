def generate_number_pyramid(rows):
    if rows <= 0:
        return []
    max_num = rows * rows
    line_width = len(str(max_num)) * rows + (rows - 1)
    lines = []
    for i in range(1, rows + 1):
        start_num = (i - 1) * (i - 1) + 1
        end_num = i * i
        numbers = [str(num) for num in range(start_num, end_num + 1)]
        center = " ".join(numbers)
        padding = (line_width - len(center)) // 2
        line = " " * padding + center
        lines.append(line)
    return lines

if __name__ == '__main__':
    result = generate_number_pyramid(7)
    for line in result:
        print(line)