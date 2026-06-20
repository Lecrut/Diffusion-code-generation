class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

if __name__ == '__main__':
    calc = Calculator()
    result_add = calc.add(10, 5)
    result_subtract = calc.subtract(10, 5)
    print(f"Addition result: {result_add}")
    print(f"Subtraction result: {result_subtract}")