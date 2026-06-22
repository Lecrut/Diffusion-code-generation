def render_hollow_triangle(rows: int) -> list[str]:
    result = []
    for i in range(1, rows + 1):
        if i == 1 or i == rows:
            result.append(" " * (rows - i) + "*" * (2 * i - 1))
        else:
            middle = 2 * i - 3
            result.append(" " * (rows - i) + "*" + " " * middle + "*")
    return result

if __name__ == "__main__":
    triangle_lines = render_hollow_triangle(8)
    for line in triangle_lines:
        print(line)