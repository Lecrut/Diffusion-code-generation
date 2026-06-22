import math
SQUARE_ROOT = math.sqrt

def find_side_length(area):
    return SQUARE_ROOT(area)
if __name__ == '__main__':
    sample_area_values = [16.0, 25.0, 36.0, 49.0, 64.0]
    for area in sample_area_values:
        side_length = find_side_length(area)
        print(f'Area: {area}, Side Length: {side_length}')