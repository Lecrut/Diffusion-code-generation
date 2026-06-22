import math

class EllipseCalculator:
    PI = math.pi

    @staticmethod
    def calculate_area(a, b):
        if a <= 0 or b <= 0:
            raise ValueError("Semi-axes must be positive")
        return EllipseCalculator.PI * a * b

if __name__ == '__main__':
    semi_major_axis = 10.5
    semi_minor_axis = 4.2
    area = EllipseCalculator.calculate_area(semi_major_axis, semi_minor_axis)
    print(area)