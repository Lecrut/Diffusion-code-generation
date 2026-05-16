import math
def calculate_triangle_area(a, b, c):
    s = (a + b + c) / 2
    if s < 0:
        return 0
    if s < a or s < b or s < c:
        return 0
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
if __name__ == '__main__':
    side_eq = 6
    area_eq = calculate_triangle_area(side_eq, side_eq, side_eq)
    side1_iso = 5
    side2_iso = 5
    side3_iso = 8
    area_iso = calculate_triangle_area(side1_iso, side2_iso, side3_iso)
    if area_eq != 0 and area_iso != 0:
        ratio = area_eq / area_iso
        print(ratio)
    else:
        print("Error: One or both triangle areas are zero.")