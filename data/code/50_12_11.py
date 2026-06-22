def generate_hollow_equilateral_triangle(height):
    if height < 1:
        return ""
    if height == 1:
        return "*"
    
    lines = []
    for row in range(1, height + 1):
        if row == 1:
            lines.append(" " * (height - 1) + "*")
        elif row == height:
            lines.append("* " * (row - 1) + "*")
        else:
            lines.append(" " * (height - row) + "*" + " " * (2 * (row - 2) + 1) + "*")
    
    return "\n".join(lines)

if __name__ == "__main__":
    sample_height = 6
    print(generate_hollow_equilateral_triangle(sample_height))