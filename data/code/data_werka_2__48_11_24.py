import math

def validate_area(area):
    if area < 0:
        raise ValueError("Area cannot be negative")

def compute_square_properties(area):
    validate_area(area)
    side_length = math.sqrt(area)
    perimeter = 4 * side_length
    return side_length, perimeter

if __name__ == '__main__':
    sample_areas = [16, 25, 9]
    for area in sample_areas:
        try:
            side_length, perimeter = compute_square_properties(area)
            print(f"Area: {area}, Side Length: {side_length}, Perimeter: {perimeter}")
        except ValueError as e:
            print(e)