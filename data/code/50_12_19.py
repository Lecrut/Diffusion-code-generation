def hollow_equilateral_triangle(n):
    if n <= 0:
        return ""
    if n == 1:
        return "*"
    lines = []
    for i in range(n):
        spaces = " " * (n - 1 - i)
        if i == 0:
            line = spaces + "*"
        elif i == n - 1:
            line = ""
            for j in range(2 * i + 1):
                if j == 0 or j == 2 * i or j % 2 == 1:
                    line += "*"
                else:
                    line += " "
        else:
            line = spaces + "*"
            inner_width = 2 * i - 1
            if inner_width > 0:
                inner = " " * (inner_width - 1)
                line += inner + "*"
            lines.append(line)
    if n > 1:
        bottom = ""
        for j in range(2 * n - 1):
            if j == 0 or j == 2 * n - 2 or j % 2 == 1:
                bottom += "*"
            else:
                bottom += " "
        lines.append(bottom)
    return "\n".join(lines)

if __name__ == '__main__':
    print(hollow_equilateral_triangle(5))