class Calculator:

    def add(self, a, b):
        return a + b
if __name__ == '__main__':
    calc = Calculator()
    print(calc.add(5, 3))
    print(calc.add(-10, -20))
    print(calc.add(0, 0))
    print(calc.add(7, -3))