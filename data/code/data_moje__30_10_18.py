import math

def calculate_circle_area(radius: float) -> float:
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_radii = [1.0, 5.5, 10.0, 0.5]
    for r in sample_radii:
        area = calculate_circle_area(r)
        print(area)