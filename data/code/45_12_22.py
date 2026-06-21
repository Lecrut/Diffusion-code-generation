import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    try:
        sample_radius1 = 5.0
        area1 = calculate_circle_area(sample_radius1)
        print(f"Area of circle with radius {sample_radius1}: {area1}")

        sample_radius2 = 10.5
        area2 = calculate_circle_area(sample_radius2)
        print(f"Area of circle with radius {sample_radius2}: {area2}")

        invalid_radius = -3.0
        area_invalid = calculate_circle_area(invalid_radius)
    except ValueError as e:
        print(e)