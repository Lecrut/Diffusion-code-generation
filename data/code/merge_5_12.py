class ValueCalculator:
    def calculate_difference(self, value1, value2):
        return value1 - value2
if __name__ == '__main__':
    calculator = ValueCalculator()
    a = 50
    b = 25
    result = calculator.calculate_difference(a, b)
    print(result)