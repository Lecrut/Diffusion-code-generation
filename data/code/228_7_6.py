import math
def calculate_triangle_properties(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return None, None
    if not (a + b > c and a + c > b and b + c > a):
        return None, None
    area = 0.5 * math.sqrt(
        ((a + b - c) * (c - a + b) * (a + c - b) * (a + b + c)) /
        (2 * (a + b + c))
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
        print("Invalid side lengths provided. The lengths do not form a valid triangle.")
    side_x = 1
    side_y = 2
    side_z = 10
    area, perimeter = calculate_triangle_properties(side_x, side_y, side_z)
    if area is not None:
        print(f"\nSide lengths: {side_x}, {side_y}, {side_z}")
        print(f"Area: {area}")
        print(f"Perimeter: {perimeter}")
    else:
        print(f"\nInvalid side lengths provided. The lengths do not form a valid triangle.")