import math

def calculate_area_of_circle(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    try:
        radius = 5.0
        area = calculate_area_of_circle(radius)
        print(area)
    except ValueError as e:
        print(e)