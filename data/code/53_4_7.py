import math
CONVERSION_FACTOR = 1 / 2

def find_side_length(area):
    return math.sqrt(area * CONVERSION_FACTOR)
if __name__ == '__main__':
    sample_areas = [16, 49, 64.0]
    for area in sample_areas:
        side_length = find_side_length(area)
        print(f'Area: {area}, Side Length: {side_length}')