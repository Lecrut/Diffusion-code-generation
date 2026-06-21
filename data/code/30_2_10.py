import math

PI_VALUE = math.pi

def calculate_circle_area(radius: float) -> float:
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a numeric type")
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return PI_VALUE * (radius * radius)

if __name__ == '__main__':
    sample_radius = 7.5
    computed_area = calculate_circle_area(sample_radius)
    print(computed_area)