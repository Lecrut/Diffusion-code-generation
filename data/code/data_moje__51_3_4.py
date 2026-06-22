def generate_number_pyramid(rows):
    half = rows
    lines = []
    for i in range(1, rows + 1):
        nums = list(range(1, i + 1))
        line_nums = nums + nums[-2::-1]
        line_str = ' '.join(str(n) for n in line_nums)
        lines.append(line_str)
    max_width = max(len(l) for l in lines)
    result = [l.center(max_width) for l in lines]
    return result

if __name__ == '__main__':
    pyramid_rows = 7
    pyramid_lines = generate_number_pyramid(pyramid_rows)
    for line in pyramid_lines:
        print(line)