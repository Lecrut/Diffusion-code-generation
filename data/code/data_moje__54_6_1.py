def generate_hollow_square(n: int) -> str:
    if n <= 0:
        return ""
    if n == 1:
        return "*"
    line_full = "*" * n
    line_hollow = "*" + " " * (n - 2) + "*"
    rows = [line_full] + [line_hollow] * (n - 2) + [line_full]
    return "\n".join(rows)

if __name__ == '__main__':
    result = generate_hollow_square(7)
    print(result)