import math

CONSTANT_PI = 3.141592653589793

class RadiusError(Exception):
    def __init__(self, value):
        self.message = f"Radius cannot be negative: {value}"
        super().__init__(self.message)

def calculate_circle_area(radius):
    if radius < 0:
        raise RadiusError(radius)
    return CONSTANT_PI * (radius ** 2)

if __name__ == '__main__':
    positive_radius = 5.0
    print(calculate_circle_area(positive_radius))
    
    zero_radius = 0.0
    print(calculate_circle_area(zero_radius))
    
    negative_radius = -4.0
    try:
        calculate_circle_area(negative_radius)
    except RadiusError as error:
        print(error.message)