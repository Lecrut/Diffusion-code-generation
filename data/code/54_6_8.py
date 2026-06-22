def hollow_square(n):
    if n < 1:
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

if __name__ == "__main__":
    print(hollow_square(5))