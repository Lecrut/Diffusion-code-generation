import math

def calculate_area(radius: float) -> float:
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    sample_radii = [3.0, 7.5, 12.0]
    for radius in sample_radii:
        area = calculate_area(radius)
        print(f"The area of a circle with radius {radius} is {area:.2f}")