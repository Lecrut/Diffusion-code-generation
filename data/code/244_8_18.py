import math

class SectorCalculator:
    @staticmethod
    def calculate_area(radius, angle):
        return 0.5 * radius ** 2 * math.radians(angle)

if __name__ == '__main__':
    calculator = SectorCalculator()
    area1 = calculator.calculate_area(7, 90)
    area2 = calculator.calculate_area(10, 60)
    total_area = area1 + area2
    print(total_area)