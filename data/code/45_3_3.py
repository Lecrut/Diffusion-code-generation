import math

def validate_radius(func):
    def wrapper(radius):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        return func(radius)
    return wrapper

@validate_radius
def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    try:
        print(calculate_circle_area(5.0))
    except ValueError as e:
        print(e)