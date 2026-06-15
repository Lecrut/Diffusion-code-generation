def generate_inverted_triangle(n):
    lines = []
    for i in range(n):
        line = ""
        padding = " " * (n - 1 - i)
        stars = "*" * (2 * i + 1)
        line = padding + stars
        lines.append(line)
    return lines
if __name__ == '__main__':
    N = 5
    pattern = generate_inverted_triangle(N)
    for line in pattern:
        print(line)