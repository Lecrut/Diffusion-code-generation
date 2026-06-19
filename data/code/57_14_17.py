import math

CIRCLE_PROPERTIES = {
    'radius': 5,
}

def compute_area(properties):
    return math.pi * properties['radius'] ** 2

if __name__ == '__main__':
    area = compute_area(CIRCLE_PROPERTIES)
    print(area)