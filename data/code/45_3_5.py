import math

def validate_radius(radius):
    if radius <= 0:
        raise ValueError("Radius must be positive")

def circle_area_decorator(func):
    def wrapper(radius):
        validate_radius(radius)
        return func(radius)
    return wrapper

@circle_area_decorator
def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    try:
        print(calculate_circle_area(5.0))
    except ValueError as e:
        print(e)