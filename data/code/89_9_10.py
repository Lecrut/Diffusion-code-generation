class BinaryEvaluator:
    ADDITION = '+'
    SUBTRACTION = '-'
    MULTIPLICATION = '*'
    DIVISION = '/'

    @staticmethod
    def evaluate_binary_op(a, b, op):
        if op == BinaryEvaluator.ADDITION:
            return a + b
        elif op == BinaryEvaluator.SUBTRACTION:
            return a - b
        elif op == BinaryEvaluator.MULTIPLICATION:
            return a * b
        elif op == BinaryEvaluator.DIVISION:
            if b != 0:
                return a / b
            else:
                raise ValueError("Division by zero is not allowed.")
        else:
            raise ValueError(f"Unsupported operation: {op}")

if __name__ == '__main__':
    evaluator = BinaryEvaluator()
    result_add = evaluator.evaluate_binary_op(10, 5, '+')
    result_sub = evaluator.evaluate_binary_op(10, 5, '-')
    result_mul = evaluator.evaluate_binary_op(10, 5, '*')
    result_div = evaluator.evaluate_binary_op(10, 5, '/')
    
    print(f"Addition: {result_add}")
    print(f"Subtraction: {result_sub}")
    print(f"Multiplication: {result_mul}")
    print(f"Division: {result_div}")