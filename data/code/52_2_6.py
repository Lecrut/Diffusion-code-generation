import math

def is_valid_radius(radius):
    return isinstance(radius, (int, float)) and radius >= 0

def calculate_circle_area(radius):
    if not is_valid_radius(radius):
        raise ValueError("Radius must be a non-negative number")
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_values = [3, 7.5, 10, -3]
    for radius in sample_values:
        try:
            area = calculate_circle_area(radius)
            print(f"The area of the circle with radius {radius} is {area:.2f}")
        except ValueError as e:
            print(e)