class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

if __name__ == '__main__':
    result_add = Calculator.add(15, 27)
    result_subtract = Calculator.subtract(10, 4)
    print(result_add)
    print(result_subtract)