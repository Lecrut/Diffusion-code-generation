import math
CIRCLE_PROPERTIES = {'radius': 5.0, 'pi': math.pi}

def calculate_circle_area():
    radius = CIRCLE_PROPERTIES['radius']
    pi_value = CIRCLE_PROPERTIES['pi']
    return pi_value * radius ** 2
if __name__ == '__main__':
    area = calculate_circle_area()
    print(area)