import math
CIRCLE_PROPERTIES = {'radius': 7.0, 'unit': 'meters'}

def calculate_area(radius):
    return math.pi * radius ** 2
if __name__ == '__main__':
    radius_value = CIRCLE_PROPERTIES['radius']
    area = calculate_area(radius_value)
    print(f"The area of the circle with radius {radius_value} {CIRCLE_PROPERTIES['unit']} is {area:.2f} square {CIRCLE_PROPERTIES['unit']}.")