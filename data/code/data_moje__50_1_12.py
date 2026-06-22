def generate_isosceles_triangle(height):
    rows = []
    for i in range(1, height + 1):
        stars = '*' * (2 * i - 1)
        spaces = ' ' * (height - i)
        row = spaces + stars + spaces
        rows.append(row)
    return '\n'.join(rows)

if __name__ == '__main__':
    print(generate_isosceles_triangle(7))