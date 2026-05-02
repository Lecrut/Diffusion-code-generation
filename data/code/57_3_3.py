import math
def calculate_triangle_area(base, height):
    area = 0.5 * base * height
    return area
if __name__ == '__main__':
    base_val = 10.5
    height_val = 8.0
    area_result = calculate_triangle_area(base_val, height_val)
    print(area_result)