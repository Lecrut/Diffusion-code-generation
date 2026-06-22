def generate_reverse_number_triangle(rows=5):
    result = []
    for i in range(1, rows + 1):
        row = list(range(rows, rows - i, -1))
        result.append(row)
    return result

if __name__ == '__main__':
    print(generate_reverse_number_triangle(5))