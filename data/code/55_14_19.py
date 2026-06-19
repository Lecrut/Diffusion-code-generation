def validate_side_length(side):
    if not isinstance(side, (int, float)):
        raise ValueError('All sides must be numeric types.')
    if side <= 0:
        raise ValueError('Side lengths must be positive numbers.')

def calculate_triangle_perimeter(a, b, c):
    validate_side_length(a)
    validate_side_length(b)
    validate_side_length(c)
    return a + b + c
if __name__ == '__main__':
    try:
        perimeter1 = calculate_triangle_perimeter(3, 4, 5)
        print(perimeter1)
        perimeter2 = calculate_triangle_perimeter(7.5, 9.2, 4.8)
        print(perimeter2)
        perimeter3 = calculate_triangle_perimeter(0, 4, 5)
        print(perimeter3)
    except ValueError as e:
        print(e)