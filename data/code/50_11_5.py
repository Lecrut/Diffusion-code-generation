def generate_isosceles_triangle(rows):
    if rows <= 0:
        return []
    pattern = []
    for i in range(1, rows + 1):
        spaces = ' ' * (rows - i)
        stars = '*' * (2 * i - 1)
        pattern.append(spaces + stars)
    return pattern

if __name__ == '__main__':
    sample_rows = 5
    result = generate_isosceles_triangle(sample_rows)
    for line in result:
        print(line)