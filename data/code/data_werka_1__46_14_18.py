def validate_side_lengths(a, b, c):
    if not all((isinstance(x, (int, float)) and x > 0 for x in [a, b, c])):
        raise ValueError('Side lengths must be positive numbers.')

def validate_triangle_inequality(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError('The given side lengths do not form a valid triangle.')

def calculate_triangle_perimeter(a, b, c):
    validate_side_lengths(a, b, c)
    validate_triangle_inequality(a, b, c)
    return a + b + c
if __name__ == '__main__':
    try:
        print(calculate_triangle_perimeter(3, 4, 5))
        print(calculate_triangle_perimeter(6, 8, 10))
        print(calculate_triangle_perimeter(7, 24, 25))
        print(calculate_triangle_perimeter(1, 1, 2))
    except ValueError as e:
        print(e)