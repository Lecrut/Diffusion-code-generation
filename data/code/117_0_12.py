class Calculator:
    def calculate_difference(self, num1, num2):
        return num1 - num2

if __name__ == '__main__':
    calc = Calculator()
    result1 = calc.calculate_difference(15, 7)
    result2 = calc.calculate_difference(3.5, 2.1)
    print(result1)
    print(result2)