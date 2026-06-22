import math
import sys

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

if __name__ == "__main__":
    sample_radius = 5
    try:
        result = calculate_circle_area(sample_radius)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)