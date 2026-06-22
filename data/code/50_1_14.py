def generate_isosceles_triangle(height=7):
    rows = []
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        stars = '*' * (2 * i - 1)
        rows.append(spaces + stars)
    return '\n'.join(rows)

if __name__ == '__main__':
    print(generate_isosceles_triangle())