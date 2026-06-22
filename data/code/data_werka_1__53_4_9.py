import math

def find_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return math.sqrt(area)

if __name__ == '__main__':
    sample_areas = [16, 25.0, 49, 64.0]
    for area in sample_areas:
        side_length = find_side_length(area)
        print(f'Area: {area}, Side Length: {side_length}')