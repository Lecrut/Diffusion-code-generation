class BinaryEvaluator:
    def evaluate_binary_op(self, a, b, op):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            if b != 0:
                return a / b
            else:
                raise ValueError("Cannot divide by zero")
        else:
            raise ValueError(f"Unsupported operation: {op}")

if __name__ == '__main__':
    evaluator = BinaryEvaluator()
    result_add = evaluator.evaluate_binary_op(5, 3, '+')
    result_sub = evaluator.evaluate_binary_op(5, 3, '-')
    result_mul = evaluator.evaluate_binary_op(5, 3, '*')
    result_div = evaluator.evaluate_binary_op(5, 3, '/')
    
    print(f"Addition (5 + 3): {result_add}")
    print(f"Subtraction (5 - 3): {result_sub}")
    print(f"Multiplication (5 * 3): {result_mul}")
    print(f"Division (5 / 3): {result_div}")