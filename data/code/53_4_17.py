import math

def find_side_length(area):
    return math.sqrt(area)

if __name__ == '__main__':
    sample_areas = [16, 25, 36.0, 49, 64.0]
    for area in sample_areas:
        side_length = find_side_length(area)
        print(f'Area: {area}, Side Length: {side_length}')