class SumCalculator:
    @staticmethod
    def sum_two_integers(a, b):
        return a + b

if __name__ == '__main__':
    calculator = SumCalculator()
    result1 = calculator.sum_two_integers(3, 5)
    print(result1)