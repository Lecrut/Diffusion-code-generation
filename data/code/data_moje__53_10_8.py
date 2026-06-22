def generate_reverse_triangle(n):
    lines = []
    for i in range(n, 0, -1):
        line = []
        for _ in range(i):
            line.append(str(i))
        lines.append(' '.join(line))
    return '\n'.join(lines)

if __name__ == '__main__':
    n = 5
    result = generate_reverse_triangle(n)
    print(result)