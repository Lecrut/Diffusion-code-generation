import math
def circle_area(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    if radius <= 0:
        raise ValueError("Radius must be positive")
    return math.pi * radius ** 2
if __name__ == '__main__':
    print(circle_area(7))
    print(circle_area(12.5))