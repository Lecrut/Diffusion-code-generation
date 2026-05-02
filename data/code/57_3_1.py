import math
def calculate_triangle_area(base, height):
    area = 0.5 * base * height
    return area
if __name__ == '__main__':
    base_value = 10.5
    height_value = 8.2
    area_result = calculate_triangle_area(base_value, height_value)
    print(area_result)