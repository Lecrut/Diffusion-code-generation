class BooleanEvaluator:

    def __init__(self):
        self.operations = {'not': lambda x: not x, 'and': lambda x, y: x and y, 'or': lambda x, y: x or y}

    @staticmethod
    def parse_expression(expression):
        return expression.replace('and', '&&').replace('or', '||').replace('not', '!')

    def evaluate(self, expression):
        tokens = self.parse_expression(expression).split()
        if not tokens:
            return False
        result_stack = []
        operator_stack = []
        for token in tokens:
            if token.isalpha() and token != 'True' and (token != 'False'):
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append('(')
            elif token == ')':
                while operator_stack[-1] != '(':
                    op = operator_stack.pop()
                    result_stack.append(self.operations[op](result_stack.pop()))
                operator_stack.pop()
            else:
                result_stack.append(token == 'True')
        while operator_stack:
            op = operator_stack.pop()
            right = result_stack.pop()
            left = result_stack.pop()
            result_stack.append(self.operations[op](left, right))
        return result_stack[0]
if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    sample_values = [('not True', False), ('True and False', False), ('True or False', True), ('(True and False) or (False and True)', False), ('not (True and False)', True)]
    for expression, expected in sample_values:
        result = evaluator.evaluate(expression)
        print(f'Expression: {expression}, Expected: {expected}, Result: {result}')