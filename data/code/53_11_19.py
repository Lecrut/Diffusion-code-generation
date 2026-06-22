def generate_reverse_number_triangle(height):
    if height <= 0:
        return []
    triangle_rows = []
    for i in range(height, 0, -1):
        row = ' '.join((str(j) for j in range(1, i + 1)))
        triangle_rows.append(row)
    return triangle_rows
if __name__ == '__main__':
    height = 5
    result = generate_reverse_number_triangle(height)
    for line in result:
        print(line)