class Calculator:
    def add(self, a, b):
        return a + b
if __name__ == '__main__':
    calc = Calculator()
    result = calc.add(5, 3)
    print(result)