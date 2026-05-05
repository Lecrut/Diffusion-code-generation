class Calculator:
    def add(self, a, b):
        return a + b
if __name__ == '__main__':
    calc = Calculator()
    result = calc.add(5, 3)
    print(result)
    result2 = calc.add(10.5, 2.5)
    print(result2)