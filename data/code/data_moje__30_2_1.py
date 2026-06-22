import math

def calculate_circle_area(radius: float) -> float:
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius * radius

if __name__ == '__main__':
    sample_radius = 5.0
    area = calculate_circle_area(sample_radius)
    print(area)

    sample_radius_two = 10.0
    area_two = calculate_circle_area(sample_radius_two)
    print(area_two)