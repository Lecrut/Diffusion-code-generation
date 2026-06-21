import math

def calculate_circle_area(radius: float) -> float:
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number.")
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    radius_value = 5
    area = calculate_circle_area(radius_value)
    print(area)