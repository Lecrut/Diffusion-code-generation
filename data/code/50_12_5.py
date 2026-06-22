def draw_hollow_equilateral_triangle(height: int) -> str:
    if height < 1:
        return ""
    if height == 1:
        return "*"
    rows = []
    rows.append(" " * (height - 1) + "*")
    for i in range(2, height):
        rows.append(" " * (height - i) + "*" + " " * (2 * i - 3) + "*")
    rows.append("*" * (2 * height - 1))
    return "\n".join(rows)

if __name__ == '__main__':
    sample_height = 5
    print(draw_hollow_equilateral_triangle(sample_height))