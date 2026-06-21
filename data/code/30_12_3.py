import math

def circle_area(radius: float) -> float:
    return math.pi * radius ** 2

if __name__ == '__main__':
    radius = 5
    area = circle_area(radius)
    print(area)