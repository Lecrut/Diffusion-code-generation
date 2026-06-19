import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_radii = [1, 3, 5, 7, 9]
    for radius in sample_radii:
        area = calculate_circle_area(radius)
        print(f"The area of a circle with radius {radius} is: {area}")