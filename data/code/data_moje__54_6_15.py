def hollow_square(n):
    if n < 1:
        return ""
    if n == 1:
        return "*"
    line_top_bottom = "*" * n
    line_middle = "*" + " " * (n - 2) + "*"
    lines = [line_top_bottom]
    if n > 2:
        lines.extend([line_middle] * (n - 2))
        lines.append(line_top_bottom)
    else:
        lines.append(line_top_bottom)
    return "\n".join(lines)

if __name__ == '__main__':
    print(hollow_square(5))
    print(hollow_square(1))
    print(hollow_square(4))