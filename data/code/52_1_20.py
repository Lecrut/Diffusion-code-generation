import math

def calculate_circle_area(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    try:
        sample_radius = 6.5
        area = calculate_circle_area(sample_radius)
        print(f"The area of the circle with radius {sample_radius} is: {area}")
    except (TypeError, ValueError) as e:
        print(e)