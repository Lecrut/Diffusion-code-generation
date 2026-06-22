def hollow_equilateral_triangle(n):
    if n < 1:
        return ""
    if n == 1:
        return "*"
    lines = []
    for i in range(n):
        if i == 0:
            lines.append(" " * (n - 1) + "*")
        elif i == n - 1:
            lines.append("* " * (n - 1))
        else:
            left_star = "*"
            right_star = "*"
            middle_spaces = " " * (2 * i - 1)
            padding = " " * (n - 1 - i)
            lines.append(padding + left_star + middle_spaces + right_star)
    return "\n".join(lines)

if __name__ == '__main__':
    print(hollow_equilateral_triangle(5))