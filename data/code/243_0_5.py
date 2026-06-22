import math

def calculate_circle_perimeter(radius: float) -> float:
    return 2 * math.pi * radius

if __name__ == '__main__':
    sample_radius = 5.0
    print(calculate_circle_perimeter(sample_radius))