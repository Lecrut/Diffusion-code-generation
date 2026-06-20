class Calculator:
    @staticmethod
    def calculate_sum(num1, num2, num3):
        return num1 + num2 + num3

if __name__ == '__main__':
    number1 = 10
    number2 = 20
    number3 = 30
    result = Calculator.calculate_sum(number1, number2, number3)
    print(result)