def generate_downward_triangle(row_count):
    lines = []
    for i in range(row_count, 0, -1):
        lines.append('*' * i)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = generate_downward_triangle(9)
    print(result)