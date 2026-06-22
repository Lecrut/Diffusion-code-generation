def generate_reverse_number_triangle(row_count):
    result = []
    for i in range(row_count, 0, -1):
        row = list(range(1, 2 * i, 2))
        row.reverse()
        result.append(row)
    return result

if __name__ == '__main__':
    N = 5
    triangle = generate_reverse_number_triangle(N)
    for row in triangle:
        print(row)