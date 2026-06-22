def calculate_area_difference(area1, area2):
    if not (isinstance(area1, (int, float)) and isinstance(area2, (int, float))):
        raise ValueError("Both areas must be numbers.")
    return abs(area1 - area2)

if __name__ == '__main__':
    area1 = 90
    area2 = 45
    print(calculate_area_difference(area1, area2))