def calculate_triangle_perimeter(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError('The sides do not form a valid triangle.')
    return a + b + c
if __name__ == '__main__':
    try:
        side1 = 3
        side2 = 4
        side3 = 5
        perimeter = calculate_triangle_perimeter(side1, side2, side3)
        print('The perimeter of the triangle is:', perimeter)
        invalid_side1 = 1
        invalid_side2 = 1
        invalid_side3 = 3
        invalid_perimeter = calculate_triangle_perimeter(invalid_side1, invalid_side2, invalid_side3)
    except ValueError as e:
        print(e)