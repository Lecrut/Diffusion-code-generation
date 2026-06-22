def generate_symmetric_reverse_triangle(rows):
    result = []
    for i in range(1, rows + 1):
        row = []
        for j in range(1, i + 1):
            row.append(str(j))
        for j in range(i - 1, 0, -1):
            row.append(str(j))
        result.append(' '.join(row))
    return '\n'.join(result)

if __name__ == '__main__':
    print(generate_symmetric_reverse_triangle(5))