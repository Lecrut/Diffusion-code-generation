import math

def area_of_circle(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    print(area_of_circle(5))
    print(area_of_circle(0))