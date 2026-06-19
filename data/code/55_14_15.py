def calculate_triangle_perimeter(a, b, c):

    def is_valid_side_length(side):
        return isinstance(side, (int, float)) and side > 0
    if not all((is_valid_side_length(side) for side in [a, b, c])):
        raise ValueError('All sides must be positive numeric types.')
    return a + b + c
if __name__ == '__main__':
    try:
        perimeter = calculate_triangle_perimeter(3, 4, 5)
        print(perimeter)
        perimeter = calculate_triangle_perimeter(7.5, 9.2, 4.8)
        print(perimeter)
        perimeter = calculate_triangle_perimeter(-3, 4, 5)
    except ValueError as e:
        print(e)