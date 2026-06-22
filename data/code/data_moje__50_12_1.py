def hollow_equilateral_triangle(n):
    if n <= 0:
        return ""
    if n == 1:
        return "*"
    lines = []
    for i in range(n):
        spaces = " " * (n - 1 - i)
        if i == 0:
            stars = "*"
        elif i == n - 1:
            stars = "* " * (n - 1) + "*"
        else:
            stars = "*" + " " * (2 * i - 1) + "*"
        lines.append(spaces + stars)
    return "\n".join(lines)

if __name__ == '__main__':
    print(hollow_equilateral_triangle(5))