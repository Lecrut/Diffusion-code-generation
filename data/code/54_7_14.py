def generate_hollow_square(n):
    if n <= 0:
        return ""
    if n == 1:
        return "*"
    top_bottom = "*" * n
    middle_row = "*" + " " * (n - 2) + "*"
    result = [top_bottom]
    for _ in range(n - 2):
        result.append(middle_row)
    result.append(top_bottom)
    return "\n".join(result)

if __name__ == '__main__':
    print(generate_hollow_square(5))
    print(generate_hollow_square(1))
    print(generate_hollow_square(10))