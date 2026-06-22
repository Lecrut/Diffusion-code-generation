def calculate_area_difference(area1, area2):
    return abs(area1 - area2)

if __name__ == '__main__':
    area1 = 60.75
    area2 = 45.25
    difference = calculate_area_difference(area1, area2)
    print(difference)