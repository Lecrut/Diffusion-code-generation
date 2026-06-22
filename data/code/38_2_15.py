import math

CONFIG = {
    'radius': 3,
    'height': 7,
    'formula_factor': 1.0 / 3.0
}

def get_volume(r, h):
    factor = CONFIG.get('formula_factor', 1.0 / 3.0)
    return factor * math.pi * (r ** 2) * h

if __name__ == '__main__':
    target_radius = CONFIG['radius']
    target_height = CONFIG['height']
    result = get_volume(target_radius, target_height)
    print(result)