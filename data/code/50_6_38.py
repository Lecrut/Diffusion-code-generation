def calculate_area_difference(area1, area2):
    if not isinstance(area1, (int, float)) or not isinstance(area2, (int, float)):
        raise ValueError("Both areas must be integers or floats.")
    return abs(area1 - area2)

if __name__ == '__main__':
    area1 = 50.5
    area2 = 30.75
    difference = calculate_area_difference(area1, area2)
    print(difference)