def generate_reverse_number_triangle(n):
    result = []
    for i in range(n, 0, -1):
        row = [str(j) for j in range(1, i + 1)]
        result.append(row)
    return result

if __name__ == '__main__':
    n = 5
    triangle = generate_reverse_number_triangle(n)
    for row in triangle:
        print(' '.join(row))