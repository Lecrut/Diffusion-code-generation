def calculate_area_difference(area1, area2):
    return abs(area1 - area2)

if __name__ == '__main__':
    area_x = 60
    area_y = 90
    difference = calculate_area_difference(area_x, area_y)
    print(difference)