def generate_reverse_triangle(height: int) -> str:
    lines = []
    for i in range(height, 0, -1):
        row = list(range(1, i + 1))
        line = ' '.join(str(n) for n in row)
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(generate_reverse_triangle(4))