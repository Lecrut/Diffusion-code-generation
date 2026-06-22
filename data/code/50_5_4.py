def generate_downward_triangle(rows):
    result = []
    for i in range(rows, 0, -1):
        row = "*" * i
        result.append(row)
    return result

if __name__ == '__main__':
    rows = 9
    triangle = generate_downward_triangle(rows)
    for line in triangle:
        print(line)