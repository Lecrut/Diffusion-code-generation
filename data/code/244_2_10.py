import math

class Ellipse:
    @staticmethod
    def area(semimajor_axis, semiminor_axis):
        return math.pi * semimajor_axis * semiminor_axis

class AreaCalculator:
    ELLIPSE1_AREA = Ellipse.area(3, 2)
    ELLIPSE2_AREA = Ellipse.area(4, 1)

    @staticmethod
    def calculate_total_area():
        return AreaCalculator.ELLIPSE1_AREA + AreaCalculator.ELLIPSE2_AREA

if __name__ == '__main__':
    total_area = AreaCalculator.calculate_total_area()
    print(total_area)