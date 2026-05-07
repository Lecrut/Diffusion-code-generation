class OperationEvaluator:
    def evaluate(self, num1, num2, operation):
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return num1 / num2
        else:
            raise ValueError("Invalid operation specified. Supported operations are +, -, *, /")
if __name__ == '__main__':
    evaluator = OperationEvaluator()
    print(f"Addition (10, 5): {evaluator.evaluate(10, 5, '+')}")
    print(f"Subtraction (10, 5): {evaluator.evaluate(10, 5, '-')}")
    print(f"Multiplication (10, 5): {evaluator.evaluate(10, 5, '*')}")
    print(f"Division (10, 5): {evaluator.evaluate(10, 5, '/')}")
    try:
        evaluator.evaluate(10, 0, '/')
    except ZeroDivisionError as e:
        print(f"Error caught: {e}")
    try:
        evaluator.evaluate(10, 5, '%')
    except ValueError as e:
        print(f"Error caught: {e}")