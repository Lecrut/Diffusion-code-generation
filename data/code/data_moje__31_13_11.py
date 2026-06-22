from math import pow

class GeometricCalculator:
    SIDES = 4

    @staticmethod
    def calculate_area(side_length):
        return int(pow(side_length, 2))

if __name__ == '__main__':
    calculator = GeometricCalculator()
    side_length = 20
    area = calculator.calculate_area(side_length)
    print(area)