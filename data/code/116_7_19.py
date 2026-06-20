class SumCalculator:
    def sum_three(self, a, b, c):
        return a + b + c

if __name__ == '__main__':
    calculator = SumCalculator()
    result = calculator.sum_three(3, 5, 7)
    print(result)