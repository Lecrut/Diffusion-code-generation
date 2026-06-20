class MathOperations:
    def multiply(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return math.prod([a, b])
        else:
            raise ValueError("Both inputs must be valid numbers")

if __name__ == '__main__':
    calculator = MathOperations()
    num1 = 15
    num2 = 7
    try:
        result = calculator.multiply(num1, num2)
        print(f"The product of {num1} and {num2} is: {result}")
    except ValueError as e:
        print(e)