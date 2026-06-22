def calculate_triangle_perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError('All sides of the triangle must be positive numbers.')
    return a + b + c
if __name__ == '__main__':
    try:
        perimeter = calculate_triangle_perimeter(3, 4, 5)
        print(perimeter)
    except ValueError as e:
        print(e)
    try:
        perimeter = calculate_triangle_perimeter(0, 4, 5)
        print(perimeter)
    except ValueError as e:
        print(e)
    try:
        perimeter = calculate_triangle_perimeter(3, -4, 5)
        print(perimeter)
    except ValueError as e:
        print(e)