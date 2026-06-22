def generate_isosceles_triangle(height):
    rows = []
    center = height // 2
    for i in range(height):
        spaces = center - i if i <= center else i - center
        stars = 2 * (height - spaces) - 1
        row = ' ' * spaces + '*' * stars
        rows.append(row)
    return '\n'.join(rows)

if __name__ == '__main__':
    result = generate_isosceles_triangle(7)
    print(result)