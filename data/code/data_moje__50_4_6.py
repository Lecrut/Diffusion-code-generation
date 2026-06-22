def render_hollow_triangle(rows=8):
    result = []
    for i in range(1, rows + 1):
        if i == rows:
            line = "* " * i
            result.append(line.strip())
        else:
            stars_in_row = 2 * i - 1
            first_star = "*"
            middle_spaces = "  " * (stars_in_row - 2) if i > 1 else ""
            last_star = "*" if i > 1 else ""
            line = first_star + middle_spaces + last_star
            result.append(line)
    return "\n".join(result)

if __name__ == '__main__':
    print(render_hollow_triangle())