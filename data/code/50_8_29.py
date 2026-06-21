AREA1 = 90
AREA2 = 45

def calculate_area_difference(area1, area2):
    return abs(area1 - area2)

if __name__ == '__main__':
    difference = calculate_area_difference(AREA1, AREA2)
    print(difference)