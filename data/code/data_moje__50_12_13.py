def hollow_equilateral_triangle(n):
    if n <= 0:
        return ""
    lines = []
    for i in range(1, n + 1):
        if i == 1:
            line = " " * (n - 1) + "*"
        elif i == n:
            line = "* " * (n - 1) + "*"
        else:
            spaces_inside = 2 * (i - 1) - 1
            if spaces_inside <= 0:
                line = " " * (n - i) + "*" + " " * spaces_inside + "*"
            else:
                line = " " * (n - i) + "*" + " " * spaces_inside + "*"
        lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    result = hollow_equilateral_triangle(5)
    print(result)