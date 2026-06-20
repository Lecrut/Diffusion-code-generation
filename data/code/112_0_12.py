class Calculator:
    def add(self, a, b):
        return a + b

if __name__ == '__main__':
    calc = Calculator()
    result1 = calc.add(5, 3)
    result2 = calc.add(10, 20)
    print(result1)
    print(result2)