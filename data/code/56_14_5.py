import math
def calculate_area_equilateral(side):
    return (math.sqrt(3) / 4) * (side ** 2)
def calculate_area_isosceles(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
if __name__ == '__main__':
    side_eq = 6
    area_eq = calculate_area_equilateral(side_eq)
    side1_iso = 5
    side2_iso = 5
    side3_iso = 8
    area_iso = calculate_area_isosceles(side1_iso, side2_iso, side3_iso)
    if area_iso == 0:
        ratio = float('inf')
    else:
        ratio = area_eq / area_iso
    print(ratio)