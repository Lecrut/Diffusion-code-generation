def generate_inverted_triangle_pattern(n):
    rows = []
    for i in range(n):
        row = ""
        for j in range(n - i):
            row += "*"
        rows.append(row)
    return rows
if __name__ == '__main__':
    N = 5
    pattern = generate_inverted_triangle_pattern(N)
    for row in pattern:
        print(row)