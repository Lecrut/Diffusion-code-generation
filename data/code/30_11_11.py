import math

AREA_FACTORS = {
    'circle': 1.0
}

def get_area_factor(shape):
    return AREA_FACTORS.get(shape, 0.0)

def calculate_area(radius, shape_type='circle'):
    factor = get_area_factor(shape_type)
    if factor == 0:
        return 0.0
    return math.pi * (radius ** 2) * factor

if __name__ == '__main__':
    test_radius = 5
    computed = calculate_area(test_radius)
    print(computed)