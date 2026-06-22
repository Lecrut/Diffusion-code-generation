class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

if __name__ == '__main__':
    result = Calculator.add(10, 5)
    print(result)