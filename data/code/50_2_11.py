def validate_area(area):
    if not isinstance(area, (int, float)):
        raise ValueError("Area must be an integer or float")

def find_difference(area1, area2):
    validate_area(area1)
    validate_area(area2)
    return abs(area1 - area2)

if __name__ == '__main__':
    area_a = 200
    area_b = 100
    difference = find_difference(area_a, area_b)
    print(difference)