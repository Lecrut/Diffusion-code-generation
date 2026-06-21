import math

PI_CONSTANT = math.pi

def calculate_circle_area(radius):
    return PI_CONSTANT * radius ** 2

if __name__ == '__main__':
    test_radius = 10.0
    result = calculate_circle_area(test_radius)
    print(result)