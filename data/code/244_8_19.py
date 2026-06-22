import math

def sector_area(radius, angle):
    return 0.5 * radius ** 2 * angle / 360

if __name__ == '__main__':
    area1 = sector_area(7, 90)
    area2 = sector_area(10, 60)
    print(area1 + area2)