class TrapezoidCalculator:
    MULTIPLIER = 0.5

    @staticmethod
    def area(base1, base2, height):
        return TrapezoidCalculator.MULTIPLIER * (base1 + base2) * height

if __name__ == '__main__':
    b1 = 8
    b2 = 12
    h = 5
    result = TrapezoidCalculator.area(b1, b2, h)
    print(result)