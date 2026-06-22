def reverse_number_triangle(rows=6):
    result = []
    for i in range(rows, 0, -1):
        row_numbers = list(range(1, i + 1))
        row_str = ' '.join(map(str, row_numbers))
        result.append(row_str)
    return '\n'.join(result)

if __name__ == '__main__':
    print(reverse_number_triangle())