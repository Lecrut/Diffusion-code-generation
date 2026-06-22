MIN_SIDE_LENGTH = 0.1

def is_valid_side_length(side):
    return isinstance(side, (int, float)) and side > MIN_SIDE_LENGTH

def calculate_triangle_perimeter(a, b, c):
    if not all((is_valid_side_length(side) for side in [a, b, c])):
        raise ValueError('All sides must be numeric types greater than 0.1.')
    return a + b + c
if __name__ == '__main__':
    try:
        perimeter = calculate_triangle_perimeter(3, 4, 5)
        print(perimeter)
    except ValueError as e:
        print(e)