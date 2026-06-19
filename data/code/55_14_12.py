def validate_numeric(value):
    if not isinstance(value, (int, float)):
        raise ValueError(f'Invalid type for side: {value}. All sides must be numeric types.')

def validate_positive(value):
    if value <= 0:
        raise ValueError(f'Invalid length for side: {value}. All sides must be positive numbers.')

def calculate_triangle_perimeter(a, b, c):
    validate_numeric(a)
    validate_numeric(b)
    validate_numeric(c)
    validate_positive(a)
    validate_positive(b)
    validate_positive(c)
    return a + b + c
if __name__ == '__main__':
    try:
        print(calculate_triangle_perimeter(3, 4, 5))
        print(calculate_triangle_perimeter(6.2, 8.1, 7.9))
        print(calculate_triangle_perimeter(-1, 4, 5))
    except ValueError as e:
        print(e)