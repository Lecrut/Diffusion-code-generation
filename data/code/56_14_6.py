import math
def calculate_area_equilateral(side):
    return (math.sqrt(3) / 4) * (side ** 2)
def calculate_area_isosceles(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
if __name__ == '__main__':
    side_eq = 6.0
    side_a = 5.0
    side_b = 5.0
    side_c = 8.0
    area_eq = calculate_area_equilateral(side_eq)
    area_iso = calculate_area_isosceles(side_a, side_b, side_c)
    if area_iso == 0:
        ratio = float('inf') if area_eq != 0 else 1.0
    else:
        ratio = area_eq / area_iso
    print(ratio)