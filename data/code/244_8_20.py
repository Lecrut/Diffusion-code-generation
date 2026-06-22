import math

def sector_area(radius, angle):
    return 0.5 * radius ** 2 * math.radians(angle)

if __name__ == '__main__':
    sectors = {
        'sector1': {'radius': 7, 'angle': 90},
        'sector2': {'radius': 10, 'angle': 60}
    }
    
    total_area = sum(sector_area(**sector) for sector in sectors.values())
    print(total_area)