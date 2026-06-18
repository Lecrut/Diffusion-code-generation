import math

def calculate_circle_area(radius: float) -> float:
    """Calculate the area of a circle given its radius using precise pi."""
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    sample_radius = 5.0
    result = calculate_circle_area(sample_radius)
    print(f"Area for radius {sample_radius}: {result}")