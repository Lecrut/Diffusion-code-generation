def calculate_triangle_perimeter(a, b, c):
    MIN_VALID_LENGTH = 0
    if a <= MIN_VALID_LENGTH or b <= MIN_VALID_LENGTH or c <= MIN_VALID_LENGTH:
        raise ValueError("Side lengths must be positive numbers.")
    return a + b + c

if __name__ == '__main__':
    try:
        perimeter = calculate_triangle_perimeter(3, 4, 5)
        print(perimeter)
    except ValueError as e:
        print(e)