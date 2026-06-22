def hollow_square(n):
    if n <= 0:
        return ""
    if n == 1:
        return "*"
    border = "*" * n
    middle = "*" + " " * (n - 2) + "*"
    lines = [border] + [middle] * (n - 2) + [border] if n > 1 else [border]
    return "\n".join(lines)

if __name__ == '__main__':
    print(hollow_square(5))
    print(hollow_square(1))
    print(hollow_square(3))