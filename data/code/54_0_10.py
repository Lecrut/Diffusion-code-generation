import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    test_radii = [2, 4, 6]
    for index, radius in enumerate(test_radii):
        area_result = calculate_circle_area(radius)
        print(f"Test {index + 1}: Radius = {radius}, Area = {area_result}")