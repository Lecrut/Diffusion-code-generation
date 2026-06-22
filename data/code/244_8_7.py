import math

def calculate_sector_area(radius, angle):
    return 0.5 * radius ** 2 * math.radians(angle)

if __name__ == '__main__':
    radius1 = 7
    angle1 = 90
    radius2 = 8
    angle2 = 45
    area1 = calculate_sector_area(radius1, angle1)
    area2 = calculate_sector_area(radius2, angle2)
    total_area = area1 + area2
    print(total_area)