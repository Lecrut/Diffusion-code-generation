class Calculator:
    DEFAULT_VALUE = 0

    @staticmethod
    def add(a, b):
        return a + b

if __name__ == '__main__':
    num1 = 20
    num2 = 30
    result = Calculator.add(num1, num2)
    print(result)