import math

def circle_area(radius: float) -> float:
    return math.pi * radius ** 2

if __name__ == '__main__':
    result = circle_area(5)
    print(result)