RECTANGLE_CONFIG = {
    'dimensions': {
        'length': 9,
        'width': 5
    }
}

def compute_perimeter(config):
    dimensions = config['dimensions']
    return 2 * (dimensions['length'] + dimensions['width'])

if __name__ == '__main__':
    perimeter = compute_perimeter(RECTANGLE_CONFIG)
    print(perimeter)