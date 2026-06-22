def generate_hollow_square(n):
    if n <= 0:
        return []
    if n == 1:
        return ["*"]
    top_bottom = "*" * n
    middle_row = "*" + " " * (n - 2) + "*"
    return [top_bottom] + [middle_row] * (n - 2) + [top_bottom]

if __name__ == '__main__':
    sample_size = 5
    result = generate_hollow_square(sample_size)
    print(result)