import math

RADIUS_PRESETS = {
    "small": 3.0,
    "medium": 7.5,
    "large": 12.0
}

def circle_area_from_radius(r):
    return math.pi * r * r

if __name__ == '__main__':
    test_radius = RADIUS_PRESETS["medium"]
    calculated_area = circle_area_from_radius(test_radius)
    print(calculated_area)