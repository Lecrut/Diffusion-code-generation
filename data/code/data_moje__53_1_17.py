def print_reverse_number_triangle(rows=4):
    result = []
    for i in range(rows, 0, -1):
        line = ''
        for j in range(1, i + 1):
            line += str(j)
        result.append(line.rjust(rows * 2 - 1))
    return '\n'.join(result)

if __name__ == '__main__':
    print(print_reverse_number_triangle(4))