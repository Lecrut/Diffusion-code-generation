import math

def find_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return math.sqrt(area)

if __name__ == '__main__':
    sample_areas = [25.0, 16.0, 9.0, 0.0, -4.0]
    for area in sample_areas:
        try:
            side_length = find_side_length(area)
            print(f'Area: {area}, Side Length: {side_length}')
        except ValueError as e:
            print(f'Area: {area}, Error: {e}')