import math

def circle_area(radius: float) -> float:
    return math.pi * radius * radius

if __name__ == '__main__':
    sample_radius = 5.0
    print(circle_area(sample_radius))

    sample_radius2 = 1.0
    print(circle_area(sample_radius2))

    sample_radius3 = 10.5
    print(circle_area(sample_radius3))