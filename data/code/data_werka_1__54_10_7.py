import math

def compute_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    try:
        print(compute_area(10))
    except ValueError as e:
        print(e)