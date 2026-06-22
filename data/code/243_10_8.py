import math

def calculate_circle_perimeter(radius: float) -> float:
    return 2 * math.pi * radius

if __name__ == '__main__':
    sample_radius = 5.0
    perimeter = calculate_circle_perimeter(sample_radius)
    print(f"Perimeter of the circle with radius {sample_radius}: {perimeter}")