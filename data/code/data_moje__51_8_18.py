def build_number_pyramid(rows):
    lines = []
    for i in range(1, rows + 1):
        digit = str(i)
        line_content = digit * i
        lines.append(line_content)
    return lines

if __name__ == '__main__':
    num_rows = 5
    pyramid_lines = build_number_pyramid(num_rows)
    for line in pyramid_lines:
        print(line)