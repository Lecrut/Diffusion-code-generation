def create_star_pattern(rows):
    pattern = []
    for i in range(1, rows + 1):
        line = '*' * i
        pattern.append(line)
    return '\n'.join(pattern)

if __name__ == '__main__':
    num_rows = 5
    star_triangle = create_star_pattern(num_rows)
    print(star_triangle)