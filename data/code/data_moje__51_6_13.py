def build_number_pyramid(levels):
    pyramid = []
    for level in range(1, levels + 1):
        row = []
        for pos in range(level):
            if pos == 0 or pos == level - 1:
                row.append(1)
            else:
                value = 0
                for i in range(level - 1):
                    if i == pos - 1 or i == pos:
                        value += 1
                row.append(value)
        pyramid.append(row)
    return pyramid

def format_pyramid_lines(pyramid):
    lines = []
    max_width = len(pyramid[-1]) * 2 - 1
    for row in pyramid:
        row_str = "  ".join(str(num) for num in row)
        line = row_str.center(max_width)
        lines.append(line)
    return lines

def print_pyramid(levels):
    pyramid = build_number_pyramid(levels)
    lines = format_pyramid_lines(pyramid)
    for line in lines:
        print(line)

if __name__ == '__main__':
    print_pyramid(4)