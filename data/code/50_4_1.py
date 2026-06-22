def render_hollow_triangle(rows: int = 8) -> str:
    if rows < 1:
        return ""
    
    lines = []
    for i in range(1, rows + 1):
        if i == 1:
            lines.append(" " * (rows - i) + "*")
        elif i == rows:
            lines.append(" " * (rows - i) + "* " * i)
            lines[-1] = lines[-1].rstrip()
        else:
            spaces = " " * (rows - i)
            inner_spaces = " " * (2 * (i - 2) - 1)
            lines.append(f"{spaces}* {inner_spaces}*")
    
    return "\n".join(lines)

if __name__ == '__main__':
    result = render_hollow_triangle(8)
    print(result)