def create_hollow_square(n):
    if n < 1:
        return ""
    if n == 1:
        return "*"
    top_bottom = "*" * n
    middle = "*" + " " * (n - 2) + "*"
    lines = [top_bottom] + [middle] * (n - 2) + [top_bottom]
    return "\n".join(lines)

if __name__ == '__main__':
    print(create_hollow_square(5))
    print(create_hollow_square(1))
    print(create_hollow_square(3))