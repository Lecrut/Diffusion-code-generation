import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_values = {'circle1': 5, 'circle2': 10.5}
    for name, radius in sample_values.items():
        area = calculate_circle_area(radius)
        print(f"Area of {name}: {area}")