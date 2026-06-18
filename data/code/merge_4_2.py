class SumCalculator:
    def find_total_sum(self, a, b, c):
        return a + b + c
if __name__ == '__main__':
    calculator = SumCalculator()
    result = calculator.find_total_sum(10, 20, 30)
    print(result)