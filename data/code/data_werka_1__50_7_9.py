def calculate_area_difference(area1, area2):
    if not isinstance(area1, (int, float)) or not isinstance(area2, (int, float)):
        raise ValueError("Both inputs must be integers or floats.")
    return abs(area1 - area2)

if __name__ == '__main__':
    try:
        area1 = 90.75
        area2 = 45.25
        difference = calculate_area_difference(area1, area2)
        print(difference)
    except ValueError as e:
        print(e)