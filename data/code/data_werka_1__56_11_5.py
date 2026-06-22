import math

def calculate_areas_and_perimeters(circle_radius1, circle_radius2, square_side1, square_side2):
    circle_area1 = math.pi * circle_radius1 ** 2
    circle_area2 = math.pi * circle_radius2 ** 2
    total_circle_area = circle_area1 + circle_area2
    square_perimeter1 = 4 * square_side1
    square_perimeter2 = 4 * square_side2
    total_square_perimeter = square_perimeter1 + square_perimeter2
    return {'total_circle_area': total_circle_area, 'total_square_perimeter': total_square_perimeter}
if __name__ == '__main__':
    circle_radius1 = 3
    circle_radius2 = 5
    square_side1 = 4
    square_side2 = 6
    result = calculate_areas_and_perimeters(circle_radius1, circle_radius2, square_side1, square_side2)
    print(result)