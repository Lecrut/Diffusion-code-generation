class Calculator:
    @staticmethod
    def calculate_difference(num1, num2):
        return round(num1 - num2, 4)

if __name__ == '__main__':
    calculator = Calculator()
    result = calculator.calculate_difference(15.0001, 7.9999)
    print(result)