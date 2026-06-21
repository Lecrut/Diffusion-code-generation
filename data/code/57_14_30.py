import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    area = math.pi * (radius ** 2)
    return area

if __name__ == '__main__':
    sample_radius = 4.25
    try:
        result = calculate_circle_area(sample_radius)
        print(f"The area of the circle with radius {sample_radius} is: {result}")
    except ValueError as e:
        print(e)