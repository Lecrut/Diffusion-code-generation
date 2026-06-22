import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    samples = [5, 0, -2]
    for r in samples:
        try:
            area = calculate_circle_area(r)
            print(area)
        except ValueError as e:
            print(e)