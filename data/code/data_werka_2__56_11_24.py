import math
PI = math.pi

def calculate_areas_and_perimeters(circle_radius1, circle_radius2, square_side1, square_side2):
    area_circle1 = PI * circle_radius1 ** 2
    area_circle2 = PI * circle_radius2 ** 2
    total_circle_area = area_circle1 + area_circle2
    perimeter_square1 = 4 * square_side1
    perimeter_square2 = 4 * square_side2
    total_square_perimeter = perimeter_square1 + perimeter_square2
    return {'total_circle_area': total_circle_area, 'total_square_perimeter': total_square_perimeter}
if __name__ == '__main__':
    circle_radius1 = 5.0
    circle_radius2 = 7.0
    square_side1 = 3.0
    square_side2 = 4.0
    result = calculate_areas_and_perimeters(circle_radius1, circle_radius2, square_side1, square_side2)
    print(result)