import math
def triangle_area_shoelace(x1, y1, x2, y2, x3, y3):
    area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    return area
if __name__ == '__main__':
    x1_val = 4
    y1_val = 3
    x2_val = 7
    y2_val = 1
    x3_val = 2
    y3_val = 5
    area_result = triangle_area_shoelace(x1_val, y1_val, x2_val, y2_val, x3_val, y3_val)
    print(area_result)