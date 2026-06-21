import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    sample_radius = 4.0
    try:
        area = calculate_circle_area(sample_radius)
        print(f"The area of the circle with radius {sample_radius} is {area:.2f}")
    except ValueError as e:
        print(e)