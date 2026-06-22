import math

def sector_area(radius, angle):
    if radius <= 0 or angle <= 0:
        raise ValueError("Radius and angle must be positive numbers")
    return 0.5 * radius ** 2 * math.radians(angle)

if __name__ == '__main__':
    try:
        area1 = sector_area(7, 90)
        area2 = sector_area(10, 60)
        total_area = area1 + area2
        print(total_area)
    except ValueError as e:
        print(e)