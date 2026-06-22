def generate_number_pyramid():
    size = 6
    rows = []
    for i in range(size):
        padding = ' ' * (size - i - 1)
        row_values = [str(i + 1) for _ in range(i + 1)]
        row_string = ' '.join(row_values)
        rows.append(padding + row_string)
    return rows

if __name__ == '__main__':
    result = generate_number_pyramid()
    for line in result:
        print(line)