def validate_area(area):
    if not isinstance(area, (int, float)):
        raise ValueError("Area must be a number")

def calculate_difference(area1, area2):
    validate_area(area1)
    validate_area(area2)
    return abs(area1 - area2)

if __name__ == '__main__':
    area_a = 300
    area_b = 450
    difference = calculate_difference(area_a, area_b)
    print(difference)