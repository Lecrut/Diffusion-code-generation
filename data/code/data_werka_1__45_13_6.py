import math

def compute_circle_area(radius):
    area = math.pi * (radius ** 2)
    return area

if __name__ == '__main__':
    radius_values = {'default': 5.0}
    radius = radius_values['default']
    area = compute_circle_area(radius)
    print(area)