def is_positive_number(value):
    return value > 0

def is_valid_triangle(a, b, c):
    return is_positive_number(a) and is_positive_number(b) and is_positive_number(c) and (a + b > c) and (a + c > b) and (b + c > a)

def calculate_triangle_perimeter(a, b, c):
    if not is_valid_triangle(a, b, c):
        raise ValueError('The given sides do not form a valid triangle')
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