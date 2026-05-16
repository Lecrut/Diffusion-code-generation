import math
def calculate_areas_and_perimeters(r1, r2, s1, s2):
    circle_area1 = math.pi * r1**2
    circle_area2 = math.pi * r2**2
    square_perimeter1 = 4 * s1
    square_perimeter2 = 4 * s2
    total_circle_area = circle_area1 + circle_area2
    total_square_perimeter = square_perimeter1 + square_perimeter2
    return {
        "total_circle_area": total_circle_area,
        "total_square_perimeter": total_square_perimeter
    }
if __name__ == '__main__':
    radius1 = 5.0
    radius2 = 3.0
    side1 = 4.0
    side2 = 6.0
    result = calculate_areas_and_perimeters(radius1, radius2, side1, side2)
    print(result)