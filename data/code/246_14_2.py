class Calculator:
    def __init__(self):
        pass
    def add(self, a, b):
        return a + b
if __name__ == '__main__':
    calc = Calculator()
    num1 = 5
    num2 = 10
    result = calc.add(num1, num2)
    print(result)