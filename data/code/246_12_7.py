class Calculator:
    @staticmethod
    def add_numbers(a, b):
        return a + b

if __name__ == '__main__':
    calculator = Calculator()
    result1 = calculator.add_numbers(3, 5)
    result2 = calculator.add_numbers(7, 9)
    print(result1, result2)