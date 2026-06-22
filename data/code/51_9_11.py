def build_symmetric_pyramid(rows: int) -> list:
    if rows <= 0:
        return []
    max_width = rows + (rows - 1)
    lines = []
    for i in range(1, rows + 1):
        space_count = max_width // 2 - (i - 1)
        number_sequence = list(range(1, i + 1))
        row_numbers = number_sequence + number_sequence[-2::-1]
        line_str = ' ' * space_count + ' '.join(str(n) for n in row_numbers)
        lines.append(line_str)
    return lines

if __name__ == '__main__':
    result = build_symmetric_pyramid(6)
    for line in result:
        print(line)