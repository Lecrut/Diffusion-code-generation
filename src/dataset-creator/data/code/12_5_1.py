class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
if __name__ == '__main__':
    calc = Calculator()
    num1 = 20
    num2 = 7
    result_add = calc.add(num1, num2)
    result_sub = calc.subtract(num1, num2)
    print(f"Addition: {result_add}")
    print(f"Subtraction: {result_sub}")