def hollow_equilateral_triangle(height):
    if height < 1:
        return ""
    if height == 1:
        return "*"
    lines = []
    width = 2 * height - 1
    lines.append(" " * (height - 1) + "*")
    for i in range(2, height):
        inner_spaces = 2 * i - 3
        lines.append(" " * (height - i) + "*" + " " * inner_spaces + "*")
    lines.append("*" * width)
    return "\n".join(lines)

if __name__ == "__main__":
    sample_height = 7
    print(hollow_equilateral_triangle(sample_height))