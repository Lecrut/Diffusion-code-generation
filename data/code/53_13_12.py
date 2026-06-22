def generate_reverse_number_triangle(rows):
    result = []
    for i in range(rows, 0, -1):
        line = " ".join(str(j) for j in range(1, i + 1))
        result.append(line)
    return result

if __name__ == '__main__':
    rows = 5
    triangle_lines = generate_reverse_number_triangle(rows)
    for line in triangle_lines:
        print(line)