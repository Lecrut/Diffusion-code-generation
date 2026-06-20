class SumCalculator:
    def add_three(self, a, b, c):
        return a + b + c

if __name__ == '__main__':
    calculator = SumCalculator()
    result1 = calculator.add_three(10, 20, 30)
    result2 = calculator.add_three(-5, -10, -15)
    print(result1)
    print(result2)