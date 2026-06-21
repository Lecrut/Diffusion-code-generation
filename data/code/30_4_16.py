import math

def circle_area(radius):
    pi_value = math.pi
    radius_squared = radius * radius
    computed_area = pi_value * radius_squared
    return computed_area

if __name__ == '__main__':
    test_radius = 10
    area_result = circle_area(test_radius)
    print(area_result)