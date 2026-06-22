def generate_reverse_number_triangle(rows: int) -> list:
    return [list(range(row, 0, -1)) for row in range(rows, 0, -1)]

if __name__ == '__main__':
    result = generate_reverse_number_triangle(5)
    for line in result:
        print(" ".join(map(str, line)))