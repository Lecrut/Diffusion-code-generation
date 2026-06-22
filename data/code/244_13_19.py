import math

class Ellipse:
    PI = math.pi
    
    @staticmethod
    def area(semi_major_axis, semi_minor_axis):
        return Ellipse.PI * semi_major_axis * semi_minor_axis

if __name__ == '__main__':
    ellipse1_area = Ellipse.area(3, 4)
    ellipse2_area = Ellipse.area(5, 6)
    total_area = ellipse1_area + ellipse2_area
    print(total_area)