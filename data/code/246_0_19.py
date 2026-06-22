class SumCalculator:
    @staticmethod
    def add_numbers(num1, num2):
        return num1 + num2

if __name__ == '__main__':
    calculator = SumCalculator()
    result = calculator.add_numbers(15, 27)
    print(result)