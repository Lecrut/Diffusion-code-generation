def generate_reverse_triangle(n):
    lines = []
    for i in range(n, 0, -1):
        line = ''.join(str(j) for j in range(1, i + 1))
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(generate_reverse_triangle(5))