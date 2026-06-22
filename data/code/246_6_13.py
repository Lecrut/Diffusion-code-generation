import sys

class SumCalculator:
    CONSTANT_A = 15
    CONSTANT_B = 27

    @staticmethod
    def calculate_total():
        return SumCalculator.CONSTANT_A + SumCalculator.CONSTANT_B

if __name__ == '__main__':
    total = SumCalculator.calculate_total()
    sys.stdout.write(str(total))