import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    area = math.pi * (radius ** 2)
    return area

if __name__ == '__main__':
    sample_radius_values = [4, 9, 12]
    for radius in sample_radius_values:
        try:
            computed_area = calculate_circle_area(radius)
            print(f"The area of a circle with radius {radius} is: {computed_area:.2f}")
        except ValueError as e:
            print(e)