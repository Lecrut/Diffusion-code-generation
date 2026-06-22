def _validate_rows(rows):
    if not isinstance(rows, int):
        raise TypeError("rows must be an integer")
    if rows < 1:
        raise ValueError("rows must be at least 1")
    return True

def build_reverse_number_triangle(rows):
    _validate_rows(rows)
    triangle = []
    number = 1
    for i in range(rows, 0, -1):
        row = [str(number + j) for j in range(i)]
        number += i
        triangle.append(row)
    return triangle

if __name__ == '__main__':
    sample_rows = 5
    result = build_reverse_number_triangle(sample_rows)
    for row in result:
        print(' '.join(row))