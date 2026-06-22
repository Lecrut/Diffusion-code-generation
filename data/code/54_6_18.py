def hollow_square(n):
    if n < 1:
        return ""
    if n == 1:
        return "*"
    top_bottom = "*" * n
    middle = "*" + " " * (n - 2) + "*"
    lines = [top_bottom]
    if n > 2:
        lines.extend([middle] * (n - 2))
    if n > 1:
        lines.append(top_bottom)
    return "\n".join(lines)

if __name__ == '__main__':
    print(hollow_square(5))
    print("---")
    print(hollow_square(1))
    print("---")
    print(hollow_square(3))