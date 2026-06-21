def validate_area(area):
    if not isinstance(area, (int, float)):
        raise ValueError("Area must be an integer or float.")

def calculate_area_difference(area1, area2):
    validate_area(area1)
    validate_area(area2)
    return abs(area1 - area2)

if __name__ == '__main__':
    sample_area1 = 75.3
    sample_area2 = 42.9
    difference = calculate_area_difference(sample_area1, sample_area2)
    print(difference)