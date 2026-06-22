def generate_inverted_triangle(size):
    if not isinstance(size, int) or size <= 0:
        return []
    rows = []
    for i in range(size, 0, -1):
        row = '*' * i
        rows.append(row)
    return rows

if __name__ == '__main__':
    result = generate_inverted_triangle(5)
    print(result)