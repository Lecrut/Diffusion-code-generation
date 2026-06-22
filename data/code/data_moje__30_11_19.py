import math

def get_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return math.pi * (radius * radius)

if __name__ == '__main__':
    print(get_circle_area(5))