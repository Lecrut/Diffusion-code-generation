class SumCalculator:
    def add_three(self, a, b, c):
        return a + b + c
if __name__ == '__main__':
    calculator = SumCalculator()
    result = calculator.add_three(10, 20, 30)
    print(result)