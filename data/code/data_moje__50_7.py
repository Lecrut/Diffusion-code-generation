def generate_star_triangle(rows: int) -> list:
    triangle = []
    for i in range(1, rows + 1):
        triangle.append('*' * i)
    return triangle

if __name__ == '__main__':
    result = generate_star_triangle(20)
    for line in result:
        print(line)