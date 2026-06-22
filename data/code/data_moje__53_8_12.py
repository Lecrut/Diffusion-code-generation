def generate_reverse_number_triangle(rows=5):
    if rows < 0:
        return []
    result = []
    current = rows
    for _ in range(rows):
        row_length = len(result) + 1
        row = list(range(current - row_length + 1, current + 1))
        result.append(row)
        current -= 1
    return result

if __name__ == '__main__':
    triangle = generate_reverse_number_triangle(5)
    print(triangle)