import math
AREA_THRESHOLD = 0

def calculate_square_side_length(area):
    if area < AREA_THRESHOLD:
        raise ValueError('Area cannot be negative')
    return math.sqrt(area)
if __name__ == '__main__':
    test_areas = [{'name': 'small_square', 'area': 16}, {'name': 'medium_square', 'area': 25}, {'name': 'large_square', 'area': 81}]
    for test in test_areas:
        side_length = calculate_square_side_length(test['area'])
        print(f"The side length of the {test['name']} is: {side_length}")