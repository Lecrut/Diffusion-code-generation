import math

def sector_area(radius, angle_degrees):
    angle_radians = math.radians(angle_degrees)
    return 0.5 * radius ** 2 * angle_radians

if __name__ == '__main__':
    area1 = sector_area(7, 90)
    area2 = sector_area(10, 60)
    total_area = area1 + area2
    print(total_area)