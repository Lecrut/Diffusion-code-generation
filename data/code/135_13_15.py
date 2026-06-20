class ExpressionEvaluator:
    def __init__(self):
        self.context = {}

    def evaluate(self, expression: str) -> bool:
        parts = expression.split()
        stack = []
        operators = {'and', 'or', 'not'}

        for part in parts:
            if part == 'True':
                stack.append(True)
            elif part == 'False':
                stack.append(False)
            elif part == 'not':
                value = stack.pop()
                stack.append(not value)
            else:
                right_value = stack.pop()
                left_value = stack.pop()
                if part == 'and':
                    stack.append(left_value and right_value)
                elif part == 'or':
                    stack.append(left_value or right_value)

        return stack[0]

    def add_to_context(self, key: str, value: bool):
        self.context[key] = value

def check_equivalence(expr1: str, expr2: str) -> bool:
    evaluator = ExpressionEvaluator()
    return evaluator.evaluate(expr1) == evaluator.evaluate(expr2)

if __name__ == '__main__':
    evaluator = ExpressionEvaluator()
    evaluator.add_to_context('a', True)
    evaluator.add_to_context('b', False)
    
    print(check_equivalence('(a and not b)', '(True and not False)'))
    print(check_equivalence('(a or b)', 'True or False'))