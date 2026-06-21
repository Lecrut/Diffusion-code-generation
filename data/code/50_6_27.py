def calculate_area_difference(area1, area2):
    return abs(area1 - area2)

if __name__ == '__main__':
    SAMPLE_AREA_1 = 75.3
    SAMPLE_AREA_2 = 45.8
    difference = calculate_area_difference(SAMPLE_AREA_1, SAMPLE_AREA_2)
    print(difference)