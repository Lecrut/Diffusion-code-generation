def generate_isosceles_triangle(rows):
    if not isinstance(rows, int) or rows <= 0:
        return []
    result = []
    max_width = 2 * rows - 1
    for i in range(1, rows + 1):
        stars = i
        spaces = (max_width - (2 * stars - 1)) // 2
        line = ' ' * spaces + '*' * (2 * stars - 1) + ' ' * spaces
        result.append(line)
    return '\n'.join(result)

if __name__ == '__main__':
    print(generate_isosceles_triangle(5))