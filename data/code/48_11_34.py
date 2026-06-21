import math

def compute_square_properties(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    side_length = math.sqrt(area)
    perimeter = 4 * side_length
    return side_length, perimeter

if __name__ == '__main__':
    square_areas = {'small_square': 16, 'medium_square': 25}
    for name, area in square_areas.items():
        try:
            side_length, perimeter = compute_square_properties(area)
            print(f"{name}: Side Length: {side_length}, Perimeter: {perimeter}")
        except ValueError as e:
            print(e)