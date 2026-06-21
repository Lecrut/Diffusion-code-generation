class BooleanEvaluator:

    @staticmethod
    def evaluate(expression):
        stack = []
        operators = {'&': lambda x, y: x & y, '|': lambda x, y: x | y, '^': lambda x, y: x ^ y}
        for char in expression:
            if char.isdigit():
                stack.append(int(char))
            elif char in operators:
                right = stack.pop()
                left = stack.pop()
                result = operators[char](left, right)
                stack.append(result)
        return stack[0]
if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    expression = '1&0|1^0'
    result = evaluator.evaluate(expression)
    print(result)