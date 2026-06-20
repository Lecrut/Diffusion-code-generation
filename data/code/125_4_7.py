class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

if __name__ == '__main__':
    calc = Calculator()
    print(calc.add(5, 3))
    print(calc.subtract(10, 4))