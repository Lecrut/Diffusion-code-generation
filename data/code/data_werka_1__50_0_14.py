def calculate_area_difference(area1, area2):
    return abs(area1 - area2)

if __name__ == '__main__':
    area1 = 500
    area2 = 300
    difference = calculate_area_difference(area1, area2)
    print(difference)