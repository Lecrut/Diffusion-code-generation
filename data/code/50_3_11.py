def print_triangle(rows):
    result = []
    for i in range(1, rows + 1):
        result.append('*' * i)
    return '\n'.join(result)

if __name__ == '__main__':
    rows = 15
    output = print_triangle(rows)
    print(output)