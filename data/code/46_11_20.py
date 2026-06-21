def calculate_triangle_perimeter(side1, side2, side3):
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        raise ValueError('Side lengths must be positive numbers.')
    return side1 + side2 + side3
if __name__ == '__main__':
    try:
        side1 = 3
        side2 = 4
        side3 = 5
        perimeter = calculate_triangle_perimeter(side1, side2, side3)
        print(perimeter)
    except ValueError as e:
        print(e)