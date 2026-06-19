RECTANGLE_CONFIG = {
    'dimensions': {
        'length': 12,
        'width': 8
    }
}

def compute_perimeter(config):
    dimensions = config['dimensions']
    length = dimensions['length']
    width = dimensions['width']
    return 2 * (length + width)

if __name__ == '__main__':
    perimeter = compute_perimeter(RECTANGLE_CONFIG)
    print(perimeter)