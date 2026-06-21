def is_positive_number(n):
    return n > 0

def forms_valid_triangle(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

def calculate_triangle_perimeter(a, b, c):
    if not is_positive_number(a) or not is_positive_number(b) or not is_positive_number(c):
        raise ValueError('Sides must be positive numbers')
    if not forms_valid_triangle(a, b, c):
        raise ValueError('The given sides do not form a valid triangle')
    return a + b + c

if __name__ == '__main__':
    side1 = 3.5
    side2 = 4.5
    side3 = 5.5
    try:
        perimeter = calculate_triangle_perimeter(side1, side2, side3)
        print(perimeter)
    except ValueError as e:
        print(e)