def hollow_square(n: int) -> str:
    if n <= 0:
        return ""
    if n == 1:
        return "*"
    top_bottom = "*" * n
    middle_row = "*" + " " * (n - 2) + "*"
    lines = [top_bottom]
    for _ in range(n - 2):
        lines.append(middle_row)
    lines.append(top_bottom)
    return "\n".join(lines)

if __name__ == '__main__':
    result = hollow_square(5)
    print(result)