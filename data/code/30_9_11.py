import math
PI_CONSTANT = math.pi
def compute_circle_area(r):
    squared_r = r * r
    area_value = PI_CONSTANT * squared_r
    return area_value
if __name__ == '__main__':
    test_radius = 3.5
    calculated_area = compute_circle_area(test_radius)
    print(calculated_area)