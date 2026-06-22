import math

def circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    print(circle_area(5))
    print(circle_area(1))
    print(circle_area(0))