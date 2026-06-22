class FactorialCalculator:
    ZERO_RESULT = 1
    INPUT_VALUE = 20

    @staticmethod
    def compute(n):
        product = 1
        for index in range(2, n + 1):
            product *= index
        return product

if __name__ == '__main__':
    calc = FactorialCalculator()
    value = calc.compute(FactorialCalculator.INPUT_VALUE)
    print(value)