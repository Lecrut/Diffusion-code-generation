import math

def get_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_values = {'radius1': 3.0, 'radius2': 7.5}
    for name, radius in sample_values.items():
        area = get_area(radius)
        print(f"The area of the circle with {name} is: {area}")