NUMERIC_TYPES = (int, float)

def validate_side_length(side):
    if not isinstance(side, NUMERIC_TYPES):
        raise ValueError('All sides must be numeric types.')
    if side <= 0:
        raise ValueError('Side lengths must be positive numbers.')

def calculate_triangle_perimeter(a, b, c):
    for side in [a, b, c]:
        validate_side_length(side)
    return a + b + c
if __name__ == '__main__':
    try:
        print(calculate_triangle_perimeter(3, 4, 5))
        print(calculate_triangle_perimeter(7.5, 9.2, 4.8))
        print(calculate_triangle_perimeter(-3, 4, 5))
    except ValueError as e:
        print(e)