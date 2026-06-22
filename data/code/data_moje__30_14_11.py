import math

def calculate_circle_area(radius: float) -> float:
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_radii = [1.0, 5.0, 10.0, 0.5, 100.0]
    for r in sample_radii:
        print(calculate_circle_area(r))