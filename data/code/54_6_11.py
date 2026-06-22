def hollow_square(n):
    if n <= 0:
        return ""
    if n == 1:
        return "*"
    top_bottom = "*" * n
    middle = "*" + " " * (n - 2) + "*"
    lines = [top_bottom]
    for _ in range(n - 2):
        lines.append(middle)
    lines.append(top_bottom)
    return "\n".join(lines)

if __name__ == '__main__':
    print(hollow_square(5))
    print(hollow_square(1))
    print(hollow_square(2))
    print(hollow_square(3))
    print(hollow_square(0))