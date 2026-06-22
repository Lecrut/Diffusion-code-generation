def generate_reverse_number_triangle(height: int = 4) -> str:
    lines = []
    for i in range(height, 0, -1):
        row = []
        for j in range(1, i + 1):
            row.append(str(j))
        lines.append(' '.join(row))
    return '\n'.join(lines)

if __name__ == '__main__':
    result = generate_reverse_number_triangle()
    print(result)