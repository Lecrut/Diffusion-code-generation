import math

GEOMETRY_SHAPES = {
    'cone': {
        'volume_formula': lambda r, h: (math.pi * r ** 2 * h) / 3,
        'params': ('radius', 'height')
    }
}

def calculate_cone_volume(radius: float, height: float) -> float:
    shape_config = GEOMETRY_SHAPES['cone']
    volume_func = shape_config['volume_formula']
    return volume_func(radius, height)

if __name__ == '__main__':
    r = 3
    h = 9
    volume = calculate_cone_volume(r, h)
    print(volume)