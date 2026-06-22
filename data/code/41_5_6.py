class RhombusCalculator:
    HALF = 0.5

    @staticmethod
    def compute_area(diagonal_a, diagonal_b):
        product = diagonal_a * diagonal_b
        return product * RhombusCalculator.HALF

if __name__ == '__main__':
    d1 = 12
    d2 = 9
    calc = RhombusCalculator()
    result = calc.compute_area(d1, d2)
    print(result)