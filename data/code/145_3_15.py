class BooleanExpressionEvaluator:

    def evaluate(self, expression):
        if not isinstance(expression, str) or not expression.strip():
            raise ValueError('Invalid expression')
        tokens = expression.split()
        result_stack = []
        operator_stack = []
        for token in tokens:
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                result_stack.append(int(token))
            elif token in ('AND', 'OR', 'NOT'):
                self._apply_operator(operator_stack, result_stack, token)
            else:
                raise ValueError(f'Invalid token: {token}')
        while operator_stack:
            self._apply_operator(operator_stack, result_stack)
        return result_stack[0]

    def _apply_operator(self, operator_stack, result_stack, op=None):
        if not operator_stack and (not op):
            return
        elif op is None:
            b = result_stack.pop()
            a = result_stack.pop()
            op = operator_stack.pop()
        else:
            b = a = result_stack.pop()
        if op == 'AND':
            result_stack.append(a & b)
        elif op == 'OR':
            result_stack.append(a | b)
        elif op == 'NOT':
            result_stack.append(~a)
if __name__ == '__main__':
    evaluator = BooleanExpressionEvaluator()
    print(evaluator.evaluate('1 AND 0'))
    print(evaluator.evaluate('1 OR 0'))
    print(evaluator.evaluate('NOT 1'))