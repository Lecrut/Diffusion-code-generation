import math

def circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    sample_radius = 3
    try:
        print(circle_area(sample_radius))
    except ValueError as e:
        print(e)