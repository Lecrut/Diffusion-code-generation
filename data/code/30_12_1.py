import math

def circle_area(radius: float) -> float:
    return math.pi * radius ** 2

if __name__ == '__main__':
    radius = 5.0
    result = circle_area(radius)
    print(result)