import math

def circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    try:
        result1 = circle_area(7.5)
        print(result1)
        result2 = circle_area(2)
        print(result2)
    except (ValueError, TypeError) as e:
        print(e)