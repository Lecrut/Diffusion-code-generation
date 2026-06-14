import math
def compare_areas(radius, side):
    circle_area = math.pi * radius**2
    square_area = side**2
    epsilon = 1e-9
    return abs(circle_area - square_area) < epsilon
if __name__ == '__main__':
    r1 = 1.0
    s1 = math.sqrt(math.pi)
    print(f"Test 1 (Expected True): {compare_areas(r1, s1)}")
    r2 = 2.0
    s2 = math.sqrt(2 * math.pi)
    print(f"Test 2 (Expected True): {compare_areas(r2, s2)}")
    r3 = 1.0
    s3 = 1.0
    print(f"Test 3 (Expected False): {compare_areas(r3, s3)}")
    r4 = 3.0
    s4 = 3.0 * math.pi / 9.0
    print(f"Test 4 (Expected True): {compare_areas(r4, s4)}")