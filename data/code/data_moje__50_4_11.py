def render_hollow_triangle(rows=8):
    if rows <= 0:
        return ""
    if rows == 1:
        return "*"
    lines = []
    for i in range(rows):
        if i == 0:
            lines.append("*")
        elif i == rows - 1:
            lines.append("*" * (2 * i + 1))
        else:
            left_star = "*"
            spaces = " " * (2 * i - 1)
            right_star = "*"
            line = left_star + spaces + right_star
            lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    result = render_hollow_triangle()
    print(result)