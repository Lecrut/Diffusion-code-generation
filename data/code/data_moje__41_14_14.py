class AreaCalculator:
    HALF = 0.5

    @staticmethod
    def compute(d1, d2):
        return AreaCalculator.HALF * d1 * d2

if __name__ == '__main__':
    val1 = 12.0
    val2 = 9.0
    output = AreaCalculator.compute(val1, val2)
    print(output)