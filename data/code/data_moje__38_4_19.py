import math

SHAPE_CONSTANTS = {
    'cone': {
        'coefficient': 1 / 3,
        'description': 'Cone volume calculation'
    }
}

def compute_cone_volume(radius, height):
    coeff = SHAPE_CONSTANTS['cone']['coefficient']
    base_area = math.pi * radius ** 2
    return coeff * base_area * height

if __name__ == '__main__':
    parameters = {'radius': 6, 'height': 9}
    calculated_volume = compute_cone_volume(parameters['radius'], parameters['height'])
    print(calculated_volume)