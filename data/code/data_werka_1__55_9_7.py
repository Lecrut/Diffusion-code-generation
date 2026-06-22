def calculate_triangle_perimeter(a, b, c):
    MIN_VALID_LENGTH = 0.1
    if a <= MIN_VALID_LENGTH or b <= MIN_VALID_LENGTH or c <= MIN_VALID_LENGTH:
        raise ValueError('Side lengths must be greater than zero.')
    return a + b + c
if __name__ == '__main__':
    try:
        side_a = 3.5
        side_b = 4.2
        side_c = 5.1
        perimeter = calculate_triangle_perimeter(side_a, side_b, side_c)
        print(perimeter)
    except ValueError as e:
        print(e)