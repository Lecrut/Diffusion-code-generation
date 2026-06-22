def reverse_number_triangle(row_count):
    result = []
    for i in range(row_count, 0, -1):
        line = ' '.join(str(j) for j in range(1, i + 1))
        result.append(line)
    return '\n'.join(result)

if __name__ == '__main__':
    hard_coded_rows = 5
    triangle_output = reverse_number_triangle(hard_coded_rows)
    print(triangle_output)