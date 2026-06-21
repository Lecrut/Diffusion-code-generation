import math

def circle_area(radius: float) -> float:
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_radius = 5.0
    area = circle_area(sample_radius)
    print(area)