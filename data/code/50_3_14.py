def generate_star_triangle(rows):
    lines = []
    for i in range(1, rows + 1):
        lines.append('*' * i)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = generate_star_triangle(15)
    print(result)