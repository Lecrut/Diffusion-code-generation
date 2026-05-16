import math
def calculate_shapes(r1, r2, s1, s2):
    circle_area = math.pi * (r1**2) + math.pi * (r2**2)
    square_perimeter = 4 * s1 + 4 * s2
    return {
        "total_circle_area": circle_area,
        "total_square_perimeter": square_perimeter
    }
if __name__ == '__main__':
    r1_val = 5.0
    r2_val = 10.0
    s1_val = 3.0
    s2_val = 7.0
    result = calculate_shapes(r1_val, r2_val, s1_val, s2_val)
    print(result)