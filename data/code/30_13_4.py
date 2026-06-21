import math
import sys

def circle_area(radius: float) -> float:
    return math.pi * radius * radius

if __name__ == '__main__':
    radius = 5.0
    area = circle_area(radius)
    print(area)