def generate_hollow_square(n):
    if n <= 0:
        return ""
    if n == 1:
        return "*"
    top_bottom = "*" * n
    middle = "*" + " " * (n - 2) + "*"
    rows = [top_bottom] + [middle] * (n - 2) + [top_bottom]
    return "\n".join(rows)

if __name__ == '__main__':
    result = generate_hollow_square(5)
    print(result)