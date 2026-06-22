def generate_right_angled_triangle(rows: int) -> str:
    return '\n'.join('*' * i for i in range(1, rows + 1))

if __name__ == '__main__':
    rows = 20
    print(generate_right_angled_triangle(rows))