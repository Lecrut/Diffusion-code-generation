import math
def calculate_area_circle(radius):
    return math.pi * radius**2
if __name__ == '__main__':
    radius_sample = 5.0
    area = calculate_area_circle(radius_sample)
    print(area)