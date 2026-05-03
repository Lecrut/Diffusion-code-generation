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
    side_a = 5
    side_b = 5
    side_c = 8
    area_iso = calculate_area_isosceles(side_a, side_b, side_c)
    if area_eq != 0:
        ratio = area_iso / area_eq
        print(ratio)
    else:
        print("Error: Area of equilateral triangle is zero.")