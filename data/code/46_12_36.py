def validate_side_length(side):
    if not isinstance(side, (int, float)):
        raise TypeError('All sides must be numbers.')
    if side <= 0:
        raise ValueError('All sides must be positive numbers.')

def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and (b + c > a)

def calculate_triangle_perimeter(a, b, c):
    validate_side_length(a)
    validate_side_length(b)
    validate_side_length(c)
    if not is_valid_triangle(a, b, c):
        raise ValueError('The given side lengths do not form a valid triangle.')
    return a + b + c
if __name__ == '__main__':
    try:
        print(calculate_triangle_perimeter(3, 4, 5))
        print(calculate_triangle_perimeter(7, 8, 9))
        print(calculate_triangle_perimeter(10, 10, 10))
        print(calculate_triangle_perimeter(1, 1, 2))
    except (TypeError, ValueError) as e:
        print(e)