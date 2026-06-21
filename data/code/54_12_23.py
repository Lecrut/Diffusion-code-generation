import math

def compute_circle_area(radius: float) -> float:
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    return math.pi * radius ** 2

if __name__ == '__main__':
    radius_value = 5.0
    area_result = compute_circle_area(radius_value)
    print(f"The area of the circle with radius {radius_value} is: {area_result}")