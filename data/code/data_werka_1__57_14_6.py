import math
CIRCLE_PROPERTIES = {'radius': 5}

def calculate_circle_area(config):
    return math.pi * config['radius'] ** 2
if __name__ == '__main__':
    area = calculate_circle_area(CIRCLE_PROPERTIES)
    print(area)