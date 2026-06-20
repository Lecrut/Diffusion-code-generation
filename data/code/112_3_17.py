class Calculator:
    @staticmethod
    def add_numbers(a, b):
        return a + b

if __name__ == '__main__':
    result = Calculator.add_numbers(15, 27)
    print(result)