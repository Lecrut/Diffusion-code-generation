class Calculator:
    @staticmethod
    def add_integers(a, b):
        return a + b

if __name__ == '__main__':
    result = Calculator.add_integers(3, 5)
    print(result)