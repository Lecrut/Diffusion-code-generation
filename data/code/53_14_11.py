def generate_reverse_number_triangle(n):
    result = []
    for i in range(n, 0, -1):
        row = list(range(1, i + 1))
        result.append(row)
    return result

def print_triangle(triangle):
    for row in triangle:
        print(' '.join(map(str, row)))

if __name__ == '__main__':
    n = 5
    triangle = generate_reverse_number_triangle(n)
    print_triangle(triangle)