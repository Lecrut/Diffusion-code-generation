def is_valid_triangle(a, b, c):
    return a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a)

def calculate_triangle_perimeter(a, b, c):
    if not is_valid_triangle(a, b, c):
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