class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

if __name__ == '__main__':
    calc = Calculator()
    print(calc.add(5, 3))
    print(calc.subtract(10, 4))