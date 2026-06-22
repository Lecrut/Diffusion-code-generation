def generate_star_triangle(rows):
    result = []
    for i in range(1, rows + 1):
        result.append('*' * i)
    return result

if __name__ == '__main__':
    sample_rows = 20
    triangle_output = generate_star_triangle(sample_rows)
    for line in triangle_output:
        print(line)