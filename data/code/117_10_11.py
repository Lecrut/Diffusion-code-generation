class PreciseCalculator:
    def calculate_difference(self, num1, num2):
        return round(num1 - num2, 4)

if __name__ == '__main__':
    calculator = PreciseCalculator()
    result = calculator.calculate_difference(15.0, 7.3)
    print(result)