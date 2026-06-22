def render_hollow_triangle(rows=8):
    if rows <= 0:
        return ""
    result = []
    for i in range(1, rows + 1):
        if i == 1:
            result.append(" " * (rows - 1) + "*")
        elif i == rows:
            result.append("* " * rows)
        else:
            spaces = " " * (rows - i)
            middle_spaces = " " * (2 * i - 3)
            result.append(f"{spaces}*{middle_spaces}*")
    return "\n".join(result)

if __name__ == '__main__':
    sample_rows = 8
    output = render_hollow_triangle(sample_rows)
    print(output)