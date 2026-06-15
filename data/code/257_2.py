class RangeCalculator:
    def get_extreme_difference(self, a, b):
        return max(a, b) - min(a, b)
if __name__ == '__main__':
    calculator = RangeCalculator()
    num1 = 10
    num2 = 5
    result = calculator.get_extreme_difference(num1, num2)
    print(result)