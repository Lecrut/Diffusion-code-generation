class Calculator:
    def add(self, a, b):
        return a + b

if __name__ == '__main__':
    calc = Calculator()
    result1 = calc.add(3, 5)
    result2 = calc.add(7.5, 2.5)
    print(result1)
    print(result2)