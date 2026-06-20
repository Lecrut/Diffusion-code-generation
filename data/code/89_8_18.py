class OperationEvaluator:

    def evaluate(self, num1, num2, operation):
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            if num2 != 0:
                return num1 / num2
            else:
                raise ValueError('Division by zero is not allowed')
        else:
            raise ValueError('Invalid operation')
if __name__ == '__main__':
    evaluator = OperationEvaluator()
    print(evaluator.evaluate(10, 5, '+'))
    print(evaluator.evaluate(10, 5, '-'))
    print(evaluator.evaluate(10, 5, '*'))
    print(evaluator.evaluate(10, 5, '/'))