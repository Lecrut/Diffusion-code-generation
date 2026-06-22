def generate_reverse_number_triangle(rows):
    result = []
    for i in range(rows, 0, -1):
        row_num = rows - i + 1
        line = ''.join(str(j) for j in range(1, i + 1))
        result.append(line)
    return '\n'.join(result)

if __name__ == '__main__':
    print(generate_reverse_number_triangle(5))