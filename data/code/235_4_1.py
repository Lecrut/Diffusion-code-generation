def generate_inverted_triangle(n):
    lines = []
    for i in range(n):
        line = ""
        for j in range(n - i):
            line += "*"
        lines.append(line)
    return lines
if __name__ == '__main__':
    N = 5
    pattern = generate_inverted_triangle(N)
    for line in pattern:
        print(line)