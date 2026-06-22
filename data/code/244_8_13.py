import math

class Sector:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self, angle):
        return 0.5 * self.radius ** 2 * math.radians(angle)

if __name__ == '__main__':
    sector1 = Sector(7)
    sector2 = Sector(10)
    
    area1 = sector1.area(90)
    area2 = sector2.area(60)
    
    total_area = area1 + area2
    print(total_area)