import math

class Ellipse:
    def __init__(self, semi_major, semi_minor):
        self.semi_major = semi_major
        self.semi_minor = semi_minor
    
    def area(self):
        return math.pi * self.semi_major * self.semi_minor

def area_ratio(ellipse1, ellipse2):
    area1 = ellipse1.area()
    area2 = ellipse2.area()
    if area1 > area2:
        return area1 / area2
    else:
        return area2 / area1

if __name__ == '__main__':
    ellipse_a = Ellipse(5, 3)
    ellipse_b = Ellipse(4, 2)
    
    ratio = area_ratio(ellipse_a, ellipse_b)
    print(ratio)