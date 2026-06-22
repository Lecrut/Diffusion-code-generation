def generate_reverse_triangle(rows):
    lines = []
    for i in range(rows, 0, -1):
        lines.append(' '.join(str(j) for j in range(1, i + 1)))
    return '\n'.join(lines)

if __name__ == '__main__':
    result = generate_reverse_triangle(5)
    print(result)