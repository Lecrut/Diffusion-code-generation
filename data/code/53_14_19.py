def generate_reverse_number_triangle(n):
    result = []
    for i in range(n, 0, -1):
        row = []
        for j in range(i):
            row.append(i)
        result.append(row)
    return result

def print_reverse_number_triangle(n):
    triangle = generate_reverse_number_triangle(n)
    for row in triangle:
        print(' '.join(map(str, row)))

if __name__ == '__main__':
    num = 5
    print_reverse_number_triangle(num)