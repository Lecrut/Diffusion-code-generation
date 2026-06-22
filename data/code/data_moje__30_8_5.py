import math

def circle_area(radius):
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    r1 = 5.0
    print(circle_area(r1))
    r2 = 3.0
    print(circle_area(r2))
    try:
        circle_area(-1.0)
    except ValueError as e:
        print(e)