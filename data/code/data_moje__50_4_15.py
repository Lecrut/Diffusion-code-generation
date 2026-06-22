def hollow_triangle(n):
    if n <= 0:
        return ""
    lines = []
    for i in range(n):
        if i == 0:
            lines.append("*")
        elif i == n - 1:
            lines.append("*" * n)
        else:
            line = " " * (n - 1 - i) + "*" + " " * (2 * i - 1) + "*"
            lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    result = hollow_triangle(8)
    print(result)