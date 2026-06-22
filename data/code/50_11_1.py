def generate_isosceles_triangle(rows):
    if rows <= 0:
        return []
    
    result = []
    for i in range(1, rows + 1):
        spaces = ' ' * (rows - i)
        stars = '*' * (2 * i - 1)
        result.append(spaces + stars)
    return result

if __name__ == '__main__':
    rows = 5
    triangle = generate_isosceles_triangle(rows)
    for line in triangle:
        print(line)