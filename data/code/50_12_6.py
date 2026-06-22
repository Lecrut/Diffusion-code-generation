def hollow_equilateral_triangle(height):
    if height <= 0:
        return ""
    if height == 1:
        return "*"
    
    lines = []
    indent_width = height - 1
    
    lines.append(" " * indent_width + "*")
    
    for row in range(2, height):
        spaces_between = 2 * (row - 1) - 1
        line = " " * (height - row) + "*" + " " * spaces_between + "*"
        lines.append(line)
    
    base_stars = " * " * (height - 1)
    if height > 1:
        lines.append(" " + base_stars + "*")
    else:
        lines[0] = "*"
    
    return "\n".join(lines)

if __name__ == '__main__':
    sample_height = 5
    result = hollow_equilateral_triangle(sample_height)
    print(result)