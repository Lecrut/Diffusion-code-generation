class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
if __name__ == '__main__':
    calc = Calculator()
    num1 = 10
    num2 = 5
    sum_result = calc.add(num1, num2)
    diff_result = calc.subtract(num1, num2)
    print(f"Addition: {sum_result}")
    print(f"Subtraction: {diff_result}")