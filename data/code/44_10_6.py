RECTANGLE_MEASUREMENTS = {
    'length': 9,
    'width': 5
}

def compute_perimeter(measurements):
    return 2 * (measurements['length'] + measurements['width'])

if __name__ == '__main__':
    perimeter = compute_perimeter(RECTANGLE_MEASUREMENTS)
    print(perimeter)