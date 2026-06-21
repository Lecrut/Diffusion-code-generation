import math

def calculate_circle_perimeter(radius):
    return 2 * math.pi * radius

if __name__ == '__main__':
    circle_properties = {'radius': 6}
    perimeter = calculate_circle_perimeter(circle_properties['radius'])
    print(perimeter)