import math

def compute_circle_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_values = {'radius1': 3, 'radius2': 7}
    for name, radius in sample_values.items():
        area = compute_circle_area(radius)
        print(f"{name} with radius {radius}: Area = {area}")