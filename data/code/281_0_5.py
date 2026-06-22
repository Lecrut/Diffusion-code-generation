class SumCalculator:

    def sum_three(self, a, b, c):
        return a + b + c
if __name__ == '__main__':
    calculator = SumCalculator()
    result1 = calculator.sum_three(1, 2, 3)
    result2 = calculator.sum_three(10, 25, 30)
    print(result1)
    print(result2)