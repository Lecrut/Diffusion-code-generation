import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    print(calculate_circle_area(5))
    try:
        print(calculate_circle_area(-3))
    except ValueError as e:
        print(e)