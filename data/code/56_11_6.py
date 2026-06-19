import math

def calculate_total_area_and_perimeter(circle_radius1, circle_radius2, square_side1, square_side2):
    total_circle_area = math.pi * (circle_radius1 ** 2) + math.pi * (circle_radius2 ** 2)
    total_square_perimeter = 4 * square_side1 + 4 * square_side2
    return {'total_circle_area': total_circle_area, 'total_square_perimeter': total_square_perimeter}

if __name__ == '__main__':
    circle_radius1 = 3.0
    circle_radius2 = 7.0
    square_side1 = 6.0
    square_side2 = 8.0

    result = calculate_total_area_and_perimeter(circle_radius1, circle_radius2, square_side1, square_side2)
    print(result)