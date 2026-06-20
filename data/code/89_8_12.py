class OperationEvaluator:

    @staticmethod
    def evaluate(num1, num2, operator):
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            if num2 != 0:
                return num1 / num2
            else:
                raise ValueError('Cannot divide by zero')
        else:
            raise ValueError('Unsupported operation')
if __name__ == '__main__':
    evaluator = OperationEvaluator()
    print(evaluator.evaluate(5, 3, '+'))
    print(evaluator.evaluate(10, 2, '-'))
    print(evaluator.evaluate(4, 2, '*'))
    try:
        print(evaluator.evaluate(10, 0, '/'))
    except ValueError as e:
        print(e)