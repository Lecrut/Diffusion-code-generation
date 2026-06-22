def validate_area(area):
    if not isinstance(area, (int, float)):
        raise ValueError("Area must be an integer or float.")
    if area < 0:
        raise ValueError("Area cannot be negative.")

def calculate_area_difference(area1, area2):
    validate_area(area1)
    validate_area(area2)
    return abs(area1 - area2)

if __name__ == '__main__':
    try:
        area1 = 45.7
        area2 = 63.2
        difference = calculate_area_difference(area1, area2)
        print(difference)
    except ValueError as e:
        print(e)