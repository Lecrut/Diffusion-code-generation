def generate_reverse_number_triangle(rows):
    result = []
    for i in range(rows, 0, -1):
        row = list(range(i, 0, -1))
        result.append(row)
    return result

def display_triangle(triangle):
    for row in triangle:
        print(' '.join(map(str, row)))

if __name__ == '__main__':
    rows = 5
    triangle = generate_reverse_number_triangle(rows)
    display_triangle(triangle)