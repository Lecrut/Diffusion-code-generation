import math

def sector_area(radius, angle):
    return 0.5 * radius ** 2 * math.radians(angle)

def calculate_total_sector_area():
    radii = [7, 10]
    angles = [90, 60]
    
    total_area = sum(sector_area(r, a) for r, a in zip(radii, angles))
    return total_area

if __name__ == '__main__':
    total_area = calculate_total_sector_area()
    print(total_area)