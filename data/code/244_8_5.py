import math

def validate_radius(radius):
    if radius <= 0:
        raise ValueError("Radius must be greater than zero.")

def validate_angle(angle):
    if angle < 0 or angle > 360:
        raise ValueError("Angle must be between 0 and 360 degrees.")

def sector_area(radius, angle):
    validate_radius(radius)
    validate_angle(angle)
    return 0.5 * radius ** 2 * math.radians(angle)

if __name__ == '__main__':
    area1 = sector_area(7, 90)
    area2 = sector_area(10, 60)
    total_area = area1 + area2
    print(total_area)