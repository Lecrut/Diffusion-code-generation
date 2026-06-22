def generate_downward_triangle(row_count):
    lines = []
    for i in range(row_count):
        stars = '*' * (row_count - i)
        lines.append(stars)
    return '\n'.join(lines)

if __name__ == '__main__':
    n = 9
    result = generate_downward_triangle(n)
    print(result)