import math
CONVERSION_FACTOR = 0.5

def find_side_length(area):
    return math.pow(area, CONVERSION_FACTOR)
if __name__ == '__main__':
    sample_areas = [16, 25, 36, 49.0]
    for area in sample_areas:
        side_length = find_side_length(area)
        print(f'Area: {area}, Side Length: {side_length}')