import math

def calculate_total_area_of_circles(radius1, radius2):
    if radius1 <= 0 or radius2 <= 0:
        raise ValueError("Radii must be positive numbers.")
    return math.pi * (radius1 ** 2) + math.pi * (radius2 ** 2)

def calculate_total_perimeter_of_squares(side1, side2):
    if side1 <= 0 or side2 <= 0:
        raise ValueError("Sides must be positive numbers.")
    return 4 * (side1 + side2)

def shapes_properties(radius1, radius2, side1, side2):
    total_circle_area = calculate_total_area_of_circles(radius1, radius2)
    total_square_perimeter = calculate_total_perimeter_of_squares(side1, side2)
    return {
        "total_circle_area": total_circle_area,
        "total_square_perimeter": total_square_perimeter
    }

if __name__ == '__main__':
    circle_radius1 = 3.0
    circle_radius2 = 7.5
    square_side1 = 6.0
    square_side2 = 8.0

    result = shapes_properties(circle_radius1, circle_radius2, square_side1, square_side2)
    print(f"Total Circle Area: {result['total_circle_area']}")
    print(f"Total Square Perimeter: {result['total_square_perimeter']}")