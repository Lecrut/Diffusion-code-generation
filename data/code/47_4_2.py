import math
def triangle_area(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return None
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
if __name__ == '__main__':
    a_val = 3
    b_val = 4
    c_val = 5
    area_val = triangle_area(a_val, b_val, c_val)
    print(area_val)
    a_val = 1
    b_val = 2
    c_val = 10
    area_val = triangle_area(a_val, b_val, c_val)
    print(area_val)
    a_val = 5
    b_val = 12
    c_val = 13
    area_val = triangle_area(a_val, b_val, c_val)
    print(area_val)