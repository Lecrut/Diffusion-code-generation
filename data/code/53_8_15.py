def generate_reverse_number_triangle():
    rows = 5
    triangle = []
    for i in range(1, rows + 1):
        row = list(range(i, 0, -1))
        triangle.append(row)
    return triangle

if __name__ == '__main__':
    result = generate_reverse_number_triangle()
    print(result)