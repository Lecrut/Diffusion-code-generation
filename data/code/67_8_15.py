class Calculator:
    def add(self, a, b):
        return a + b

if __name__ == '__main__':
    CALCULATOR = Calculator()
    RESULT = CALCULATOR.add(10, 20)
    print(RESULT)