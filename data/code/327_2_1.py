class Calculator:
    def __init__(self):
        pass
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
if __name__ == '__main__':
    calc = Calculator()
    num1 = 20
    num2 = 5
    sum_result = calc.add(num1, num2)
    diff_result = calc.subtract(num1, num2)
    prod_result = calc.multiply(num1, num2)
    div_result = calc.divide(num1, num2)
    print(f"Addition: {num1} + {num2} = {sum_result}")
    print(f"Subtraction: {num1} - {num2} = {diff_result}")
    print(f"Multiplication: {num1} * {num2} = {prod_result}")
    print(f"Division: {num1} / {num2} = {div_result}")
    try:
        calc.divide(10, 0)
    except ZeroDivisionError as e:
        print(f"Error caught: {e}")