import math

def calculate_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    try:
        print(calculate_area(10))
    except ValueError as e:
        print(e)