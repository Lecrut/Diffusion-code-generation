import math

def circle_area(radius: float) -> float:
    return math.pi * radius * radius

if __name__ == '__main__':
    print(circle_area(5.0))
    print(circle_area(10.0))
    print(circle_area(0.0))