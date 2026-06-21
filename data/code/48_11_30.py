import math

def compute_square_properties(area):
    side_length = area ** 0.5
    perimeter = 4 * side_length
    return side_length, perimeter

if __name__ == '__main__':
    sample_areas = [16, 25, 36]
    for index, area in enumerate(sample_areas):
        side_length, perimeter = compute_square_properties(area)
        print(f"Sample {index + 1}: Area: {area}, Side Length: {side_length}, Perimeter: {perimeter}")