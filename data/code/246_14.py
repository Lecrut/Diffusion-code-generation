class Calculator:
    def __init__(self):
        pass
    def add(self, a, b):
        return a + b
if __name__ == '__main__':
    calc = Calculator()
    num1 = 10
    num2 = 5
    result = calc.add(num1, num2)
    print(f"The sum of {num1} and {num2} is: {result}")