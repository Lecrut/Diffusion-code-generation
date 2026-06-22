def find_area_difference(area1, area2):
    if not (isinstance(area1, (int, float)) and isinstance(area2, (int, float))):
        raise ValueError("Both area1 and area2 must be numbers.")
    return abs(area1 - area2)

if __name__ == '__main__':
    area1 = 70
    area2 = 35
    difference = find_area_difference(area1, area2)
    print(difference)