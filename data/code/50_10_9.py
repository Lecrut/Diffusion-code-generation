def build_triangle_rows(levels):
    star_char = '*'
    row_map = {
        'marker': star_char,
        'separator': '\n'
    }
    lines = []
    count = 0
    while count < levels:
        line_width = count + 1
        line_content = row_map['marker'] * line_width
        lines.append(line_content)
        count += 1
    return lines

def format_triangle_output(rows):
    row_map = {
        'separator': '\n'
    }
    if not rows:
        return ''
    return row_map['separator'].join(rows)

if __name__ == '__main__':
    height = 4
    rows = build_triangle_rows(height)
    output = format_triangle_output(rows)
    print(output)