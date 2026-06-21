import math

PI_CONSTANT = math.pi
EXPONENT = 2

def compute_circle_area(radius):
    return PI_CONSTANT * (radius ** EXPONENT)

if __name__ == '__main__':
    radius_value = 3
    area_value = compute_circle_area(radius_value)
    print(area_value)