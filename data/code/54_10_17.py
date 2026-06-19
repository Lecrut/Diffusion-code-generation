import math

CIRCLE_AREA_CONSTANT = math.pi

def compute_area(radius):
    return CIRCLE_AREA_CONSTANT * radius ** 2

if __name__ == '__main__':
    test_radius = 10
    print(compute_area(test_radius))