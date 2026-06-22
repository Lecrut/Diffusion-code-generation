class Calculator:

    def add(self, a, b):
        return a + b
if __name__ == '__main__':
    calc = Calculator()
    print(calc.add(5, 3))
    print(calc.add(-1, -1))
    print(calc.add(0, 0))
    print(calc.add(-5, 5))
    print(calc.add(100, 200))