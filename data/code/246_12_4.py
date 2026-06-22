class Calculator:
    @staticmethod
    def add_numbers(a, b):
        return a + b

if __name__ == '__main__':
    calculator = Calculator()
    result = calculator.add_numbers(3, 5)
    print(result)