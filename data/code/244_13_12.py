import math

class Ellipse:
    @staticmethod
    def area(semi_major_axis, semi_minor_axis):
        return math.pi * semi_major_axis * semi_minor_axis

if __name__ == '__main__':
    total_area = Ellipse.area(3, 4) + Ellipse.area(5, 6)
    print(total_area)