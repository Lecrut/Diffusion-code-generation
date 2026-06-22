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
            line = spaces + "* " * i
            line = line.rstrip()
        else:
            inner = " " * (2 * i - 1)
            line = spaces + "*" + inner + "*"
        lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    print(hollow_equilateral_triangle(5))