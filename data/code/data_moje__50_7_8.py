def generate_right_angled_triangle(rows: int = 20) -> str:
    lines = []
    for i in range(1, rows + 1):
        lines.append('*' * i)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(generate_right_angled_triangle(20))