def hollow_equilateral_triangle(n: int) -> str:
    if n <= 0:
        return ""
    if n == 1:
        return "*"
    lines = []
    for i in range(n):
        if i == 0:
            line = " " * (n - 1) + "*"
        elif i == n - 1:
            line = ""
            for j in range(n):
                if j == 0 or j == n - 1 or i + j == n - 1:
                    line += "*"
                else:
                    line += " "
        else:
            left_spaces = n - 1 - i
            inner_spaces = i * 2 - 1
            if inner_spaces < 1:
                line = " " * left_spaces + "*" + " " * left_spaces
            else:
                line = " " * left_spaces + "*" + " " * inner_spaces + "*" + " " * left_spaces
        lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    print(hollow_equilateral_triangle(5))