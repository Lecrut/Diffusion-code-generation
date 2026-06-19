import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    try:
        radius_value = 5.0
        area = calculate_circle_area(radius_value)
        print(area)
    except ValueError as e:
        print(e)