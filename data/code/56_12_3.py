import math
def calculate_shapes(r1, r2, s1, s2):
    circle_area = math.pi * (r1**2) + math.pi * (r2**2)
    square_perimeter = 4 * s1 + 4 * s2
    return {
        "total_circle_area": circle_area,
        "total_square_perimeter": square_perimeter
    }
if __name__ == '__main__':
    radius1 = 5.0
    radius2 = 3.0
    side1 = 4.0
    side2 = 6.0
    result = calculate_shapes(radius1, radius2, side1, side2)
    print(result)