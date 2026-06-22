MAX_ROWS = 15
STAR_CHARACTER = '*'
LINE_SEPARATOR = '\n'

def build_triangle_lines(count):
    lines = []
    for length in range(1, count + 1):
        lines.append(STAR_CHARACTER * length)
    return lines

def print_left_aligned_triangle(row_count):
    lines = build_triangle_lines(row_count)
    print(LINE_SEPARATOR.join(lines))

if __name__ == '__main__':
    print_left_aligned_triangle(MAX_ROWS)