class RhombusCalculator:
    HALF = 0.5
    @staticmethod
    def area(d1, d2):
        return RhombusCalculator.HALF * d1 * d2
if __name__ == '__main__':
    d1 = 6.0
    d2 = 8.0
    print(RhombusCalculator.area(d1, d2))