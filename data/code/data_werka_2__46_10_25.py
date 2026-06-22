def validate_sides(a, b, c):
    if not (a > 0 and b > 0 and c > 0):
        raise ValueError('Sides must be positive numbers')
    if not ((a + b > c) and (a + c > b) and (b + c > a)):
        raise ValueError('The given sides do not form a valid triangle')

def calculate_triangle_perimeter(a, b, c):
    validate_sides(a, b, c)
    return a + b + c

if __name__ == '__main__':
    side1 = 5.0
    side2 = 6.0
    side3 = 7.0
    try:
        perimeter = calculate_triangle_perimeter(side1, side2, side3)
        print(perimeter)
    except ValueError as e:
        print(e)