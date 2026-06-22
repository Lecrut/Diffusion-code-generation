def create_reverse_number_triangle(n):
    rows = []
    for i in range(n, 0, -1):
        row = ' '.join(str(j) for j in range(1, i + 1))
        rows.append(row)
    return '\n'.join(rows)

if __name__ == '__main__':
    n = 5
    result = create_reverse_number_triangle(n)
    print(result)