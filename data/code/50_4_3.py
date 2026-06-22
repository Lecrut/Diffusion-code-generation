def hollow_triangle(n):
    if n <= 0:
        return ""
    lines = []
    for i in range(n):
        if i == 0:
            lines.append("*")
        elif i == n - 1:
            lines.append("*" * (2 * i + 1))
        else:
            inner_spaces = 2 * i - 1
            line = "*" + " " * inner_spaces + "*"
            lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    print(hollow_triangle(8))