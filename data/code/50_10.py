import math
def calculate_absolute_difference(area1, area2):
    return abs(area1 - area2)
if __name__ == '__main__':
    area_a = 150
    area_b = 225
    difference = calculate_absolute_difference(area_a, area_b)
    print(difference)