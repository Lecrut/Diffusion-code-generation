class Calculator:
    def add(self, a, b):
        return a + b

if __name__ == '__main__':
    calc = Calculator()
    num1 = 15
    num2 = -7
    result = calc.add(num1, num2)
    print(result)