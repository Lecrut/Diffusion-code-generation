def calculate_triangle_perimeter(side1, side2, side3):
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        raise ValueError('All sides must be positive numbers')
    return side1 + side2 + side3
if __name__ == '__main__':
    a = 7
    b = 9
    c = 10
    try:
        triangle_perimeter = calculate_triangle_perimeter(a, b, c)
        print(f'The perimeter of the triangle with sides {a}, {b}, and {c} is: {triangle_perimeter}')
    except ValueError as e:
        print(e)