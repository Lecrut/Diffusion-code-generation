def generate_hollow_triangle(n):
    if n <= 0:
        return []
    rows = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, i + 1):
            if i == n or j == 1 or j == i:
                char = chr(ord('A') + (j - 1) % 26)
                row.append(char)
            else:
                row.append(' ')
        rows.append(''.join(row))
    return rows

if __name__ == '__main__':
    result = generate_hollow_triangle(5)
    for line in result:
        print(line)