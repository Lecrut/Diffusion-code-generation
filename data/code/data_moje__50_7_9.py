def generate_star_triangle(rows: int) -> list[str]:
    return ["*" * i for i in range(1, rows + 1)]

if __name__ == '__main__':
    sample_rows = 20
    triangle = generate_star_triangle(sample_rows)
    for line in triangle:
        print(line)