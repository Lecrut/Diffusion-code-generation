def generate_reverse_number_triangle(rows):
    result = []
    for i in range(rows, 0, -1):
        row = list(range(1, i + 1))
        result.append(row)
    return result

if __name__ == '__main__':
    rows = 5
    triangle = generate_reverse_number_triangle(rows)
    for row in triangle:
        print(row)