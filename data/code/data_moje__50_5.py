def draw_downward_triangle(rows):
    result = []
    for i in range(rows, 0, -1):
        row = ' '.join(['*'] * i)
        result.append(row)
    return '\n'.join(result)

if __name__ == '__main__':
    row_count = 9
    output = draw_downward_triangle(row_count)
    print(output)