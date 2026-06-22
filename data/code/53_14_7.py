def generate_reverse_number_triangle(n):
    lines = []
    for i in range(n, 0, -1):
        line = ''.join(str(j) for j in range(1, i + 1))
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    n = 5
    print(generate_reverse_number_triangle(n))