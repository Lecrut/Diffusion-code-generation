def generate_isosceles_triangle(rows: int) -> list[str]:
    triangle = []
    for i in range(rows):
        spaces = " " * (rows - i - 1)
        stars = "*" * (2 * i + 1)
        triangle.append(spaces + stars)
    return triangle

if __name__ == '__main__':
    sample_rows = 5
    result = generate_isosceles_triangle(sample_rows)
    print(result)