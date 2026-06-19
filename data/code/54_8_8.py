import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_values = [1, 5, 10]
    for radius in sample_values:
        area = calculate_circle_area(radius)
        print(f"The area of a circle with radius {radius} is: {area}")