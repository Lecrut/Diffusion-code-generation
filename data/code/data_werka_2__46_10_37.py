def calculate_triangle_perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError('Sides must be positive numbers')
    is_valid = (a + b > c) and (a + c > b) and (b + c > a)
    if not is_valid:
        raise ValueError('The given sides do not form a valid triangle')
    return a + b + c

if __name__ == '__main__':
    side1 = 5.0
    side2 = 12.0
    side3 = 13.0
    try:
        perimeter = calculate_triangle_perimeter(side1, side2, side3)
        print(perimeter)
    except ValueError as e:
        print(e)