def calculate_area_difference(area1, area2):
    return abs(area1 - area2)

if __name__ == '__main__':
    area1 = 50.5
    area2 = 30.2
    difference = calculate_area_difference(area1, area2)
    print(difference)