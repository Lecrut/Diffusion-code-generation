import math

class Ellipse:
    @staticmethod
    def area(semi_major_axis, semi_minor_axis):
        return math.pi * semi_major_axis * semi_minor_axis

if __name__ == '__main__':
    ellipse1 = Ellipse()
    area1 = ellipse1.area(3, 4)
    ellipse2 = Ellipse()
    area2 = ellipse2.area(5, 6)
    total_area = area1 + area2
    print(total_area)