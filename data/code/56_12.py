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
    r1_val = 5.0
    r2_val = 10.0
    s1_val = 3.0
    s2_val = 7.0
    result = calculate_areas_and_perimeters(r1_val, r2_val, s1_val, s2_val)
    print(result)