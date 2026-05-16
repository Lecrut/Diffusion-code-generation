import math
def calculate_triangle_area(base, height):
    return 0.5 * base * height
if __name__ == '__main__':
    base_val = 10.0
    height_val = 5.0
    area = calculate_triangle_area(base_val, height_val)
    print(area)