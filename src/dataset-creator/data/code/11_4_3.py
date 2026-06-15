class Calculator:
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
    print(f"Addition: {calc.add(num1, num2)}")
    print(f"Subtraction: {calc.subtract(num1, num2)}")
    print(f"Multiplication: {calc.multiply(num1, num2)}")
    try:
        result_division = calc.divide(num1, 0)
        print(f"Division (Error Test): {result_division}")
    except ZeroDivisionError as e:
        print(f"Division Error Caught: {e}")
    num3 = 10
    num4 = 2
    print(f"\nDivision: {calc.divide(num3, num4)}")