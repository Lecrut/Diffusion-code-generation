import math

def get_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_values = {'circle1': 5.0, 'circle2': 10.0}
    for name, radius in sample_values.items():
        area = get_area(radius)
        print(f"The area of {name} with radius {radius} is: {area}")