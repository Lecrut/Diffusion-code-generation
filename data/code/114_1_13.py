class ArithmeticOperations:
    def multiply_two_numbers(self, a, b):
        return a * b

if __name__ == '__main__':
    calculator = ArithmeticOperations()
    num1 = 12345678901234567890
    num2 = 98765432109876543210
    result = calculator.multiply_two_numbers(num1, num2)
    print(result)