import math
area_to_side_mapping = {9: 3, 16: 4, 25: 5, 36: 6}

def find_side_length(area):
    if area in area_to_side_mapping:
        return area_to_side_mapping[area]
    return math.sqrt(area)
if __name__ == '__main__':
    sample_areas = [9, 16, 25, 30.25, 40.0]
    for area in sample_areas:
        side_length = find_side_length(area)
        print(f'Area: {area}, Side Length: {side_length}')