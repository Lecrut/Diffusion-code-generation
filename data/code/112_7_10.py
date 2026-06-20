class Calculator:
    @staticmethod
    def add_values(a, b):
        return a + b

if __name__ == '__main__':
    num1 = 7
    num2 = 3
    result = Calculator.add_values(num1, num2)
    print(result)