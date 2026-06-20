class Calculator:
    def add(self, a, b):
        return a + b

if __name__ == '__main__':
    calc = Calculator()
    result1 = calc.add(3.5, 2.7)
    result2 = calc.add(-1.2, 4.8)
    print(result1)
    print(result2)