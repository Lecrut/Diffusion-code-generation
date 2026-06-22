def print_star_triangle(rows):
    pattern = []
    for i in range(1, rows + 1):
        row = '*' * i
        pattern.append(row)
    return '\n'.join(pattern)

if __name__ == '__main__':
    num_rows = 5
    triangle_pattern = print_star_triangle(num_rows)
    print(triangle_pattern)