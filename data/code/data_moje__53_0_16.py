def generate_reverse_triangle(rows):
    return [
        ' ' * (rows - i) + str(i) * i
        for i in range(rows, 0, -1)
    ]

if __name__ == '__main__':
    sample_rows = 5
    result = generate_reverse_triangle(sample_rows)
    for line in result:
        print(line)