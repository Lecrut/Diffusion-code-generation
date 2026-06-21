import math

def circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    radius_value = 5.0
    area = circle_area(radius_value)
    print(area)