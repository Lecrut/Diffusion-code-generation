def calculate_area_difference(area1, area2):
    return abs(area1 - area2)

if __name__ == '__main__':
    first_area = 400
    second_area = 180
    difference = calculate_area_difference(first_area, second_area)
    print(difference)