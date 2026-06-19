import sys

def calculate_area_difference(area1, area2):
    return abs(area1 - area2)
if __name__ == '__main__':
    area1 = 50.0
    area2 = 30.0
    difference = calculate_area_difference(area1, area2)
    print(f'The difference between the two areas is: {difference}')