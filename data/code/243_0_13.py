import math

def validate_radius(radius: float) -> None:
    if radius <= 0:
        raise ValueError("Radius must be greater than zero.")

def calculate_circumference(radius: float) -> float:
    validate_radius(radius)
    return 2 * math.pi * radius

if __name__ == '__main__':
    sample_radius = 5.0
    circumference = calculate_circumference(sample_radius)
    print(circumference)