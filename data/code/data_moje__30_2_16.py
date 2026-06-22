import math

def calculate_circle_area(radius: float) -> float:
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    sample_radius_1 = 5.0
    sample_radius_2 = 10.5
    print(calculate_circle_area(sample_radius_1))
    print(calculate_circle_area(sample_radius_2))