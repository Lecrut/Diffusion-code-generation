def is_valid_triangle(side1, side2, side3):
    return side1 > 0 and side2 > 0 and side3 > 0 and (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1)

def calculate_triangle_perimeter(side1, side2, side3):
    if not is_valid_triangle(side1, side2, side3):
        raise ValueError("Invalid triangle sides")
    return side1 + side2 + side3

if __name__ == '__main__':
    try:
        side1 = 7
        side2 = 9
        side3 = 12
        perimeter = calculate_triangle_perimeter(side1, side2, side3)
        print(perimeter)
    except ValueError as e:
        print(e)