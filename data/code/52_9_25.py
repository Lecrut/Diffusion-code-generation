import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    sample_values = {
        'tiny': 0.5,
        'regular': 3,
        'huge': 12
    }
    for category, radius in sample_values.items():
        try:
            area = calculate_circle_area(radius)
            print(f"The area of a {category} circle with radius {radius} is: {area:.2f}")
        except ValueError as e:
            print(e)