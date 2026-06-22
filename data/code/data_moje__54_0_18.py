def generate_hollow_square(n):
    if n <= 0:
        return ""
    if n == 1:
        return "*"
    first_row = "*" * n
    middle_row = "*" + " " * (n - 2) + "*"
    last_row = first_row
    lines = [first_row]
    for _ in range(n - 2):
        lines.append(middle_row)
    lines.append(last_row)
    return "\n".join(lines)

if __name__ == '__main__':
    size = 5
    result = generate_hollow_square(size)
    print(result)