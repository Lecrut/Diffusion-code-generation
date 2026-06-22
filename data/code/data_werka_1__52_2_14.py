import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    test_radii = [2, 6.5, 12]
    for index, radius in enumerate(test_radii, start=1):
        area_result = calculate_circle_area(radius)
        print(f"Test Case {index}: Radius = {radius}, Area = {area_result:.2f}")