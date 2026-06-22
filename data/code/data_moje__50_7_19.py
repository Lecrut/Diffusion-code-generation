def generate_star_triangle(rows: int) -> list[str]:
    return ["*" * i for i in range(1, rows + 1)]

if __name__ == '__main__':
    sample_rows = 20
    result = generate_star_triangle(sample_rows)
    for line in result:
        print(line)