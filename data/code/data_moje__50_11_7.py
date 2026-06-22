def generate_isosceles_triangle(rows):
    result = []
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        stars = "*" * (2 * i - 1)
        result.append(spaces + stars)
    return "\n".join(result)

if __name__ == '__main__':
    rows = 5
    print(generate_isosceles_triangle(rows))