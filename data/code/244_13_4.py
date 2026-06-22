import math

class Ellipse:
    def __init__(self, semi_major_axis, semi_minor_axis):
        self.semi_major_axis = semi_major_axis
        self.semi_minor_axis = semi_minor_axis
    
    def area(self):
        return math.pi * self.semi_major_axis * self.semi_minor_axis

if __name__ == '__main__':
    ellipse1 = Ellipse(3, 4)
    ellipse2 = Ellipse(5, 6)
    
    area1 = ellipse1.area()
    area2 = ellipse2.area()
    
    total_area = area1 + area2
    print(total_area)