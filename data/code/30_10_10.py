import math

def circle_area(radius):
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    print(circle_area(5))
    print(circle_area(0))
    print(circle_area(7.5))