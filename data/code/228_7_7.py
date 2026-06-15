import math
def calculate_triangle_properties(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return None, None
    if not (a + b > c and a + c > b and b + c > a):
        return None, None
    area = 0.5 * math.sqrt(
        (a + b - c) * (b + c - a) * (c + a - b)
    )
    perimeter = a + b + c
    return area, perimeter
if __name__ == '__main__':
    side_a = 3
    side_b = 4
    side_c = 5
    area, perimeter = calculate_triangle_properties(side_a, side_b, side_c)
    if area is not None:
        print(f"Side lengths: {side_a}, {side_b}, {side_c}")
        print(f"Area: {area}")
        print(f"Perimeter: {perimeter}")
    else:
        print("Invalid side lengths provided. The given lengths do not form a valid triangle.")
    side_a_invalid = 1
    side_b_invalid = 2
    side_c_invalid = 10
    area_invalid, perimeter_invalid = calculate_triangle_properties(side_a_invalid, side_b_invalid, side_c_invalid)
    if area_invalid is not None:
        print(f"\nSide lengths: {side_a_invalid}, {side_b_invalid}, {side_c_invalid}")
        print(f"Area: {area_invalid}")
        print(f"Perimeter: {perimeter_invalid}")
    else:
        print(f"\nSide lengths: {side_a_invalid}, {side_b_invalid}, {side_c_invalid}")
        print("Invalid side lengths provided. The given lengths do not form a valid triangle.")