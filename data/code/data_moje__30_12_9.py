import math

def circle_area(radius: float) -> float:
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    radius = 5.0
    area = circle_area(radius)
    print(area)