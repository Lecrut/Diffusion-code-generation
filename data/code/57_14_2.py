import math

CIRCLE_CONFIG = {
    'radius': 5,
}

def calculate_area(config):
    return math.pi * config['radius'] ** 2

if __name__ == '__main__':
    area = calculate_area(CIRCLE_CONFIG)
    print(area)