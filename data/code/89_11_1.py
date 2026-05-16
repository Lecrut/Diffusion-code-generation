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
            raise ValueError("Invalid operation specified. Must be one of '+', '-', '*', or '/'")
if __name__ == '__main__':
    evaluator = OperationEvaluator()
    result_add = evaluator.evaluate(10, 5, '+')
    print(f"10 + 5 = {result_add}")
    result_sub = evaluator.evaluate(10, 5, '-')
    print(f"10 - 5 = {result_sub}")
    result_mul = evaluator.evaluate(10, 5, '*')
    print(f"10 * 5 = {result_mul}")
    result_div = evaluator.evaluate(20, 4, '/')
    print(f"20 / 4 = {result_div}")
    try:
        evaluator.evaluate(10, 0, '/')
    except ZeroDivisionError as e:
        print(f"Error caught: {e}")
    try:
        evaluator.evaluate(10, 5, '%')
    except ValueError as e:
        print(f"Error caught: {e}")