class Calculator:
    def add(self, num1, num2):
        return num1 + num2

if __name__ == '__main__':
    calc = Calculator()
    result = calc.add(15, 27)
    print(result)