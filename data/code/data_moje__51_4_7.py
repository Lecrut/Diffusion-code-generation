def generate_number_pyramid():
    rows = 3
    max_width = (rows * 2 - 1) * 2 + 2
    lines = []
    for i in range(1, rows + 1):
        line = ''
        for j in range(1, i + 1):
            line += str(j)
        padded_line = line.rjust(i)
        center_line = padded_line.center(max_width)
        lines.append(center_line)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = generate_number_pyramid()
    print(result)