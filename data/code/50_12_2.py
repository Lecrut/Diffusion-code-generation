def hollow_equilateral_triangle(n: int) -> str:
    if n == 1:
        return "*"
    if n <= 0:
        return ""
    lines = []
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        if i == 1:
            line = spaces + "*"
        elif i == n:
            line = spaces + "*" + ("* " * (i - 1)).rstrip()
        else:
            line = spaces + "*" + (" " * (2 * (i - 1) - 1)) + "*"
        lines.append(line)
    return "\n".join(lines)

if __name__ == "__main__":
    height = 7
    print(hollow_equilateral_triangle(height))