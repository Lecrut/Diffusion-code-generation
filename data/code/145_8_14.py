class PredicateEvaluator:

    def __init__(self, values):
        self.values = {f'v{i}': val for i, val in enumerate(values)}

    def evaluate(self, expression):
        tokens = expression.split()
        if not tokens:
            raise ValueError('Empty expression')

        def evaluate_term(tokens_list):
            if not tokens_list:
                return (None, [])
            token = tokens_list.pop(0)
            if token.isdigit():
                return (int(token), tokens_list)
            elif token in self.values:
                return (self.values[token], tokens_list)
            else:
                raise NameError(f'Undefined variable or constant: {token}')

        def parse_expression(tokens):
            stack = []
            for token in tokens:
                if token in ('and', 'or'):
                    right, tokens = evaluate_term(tokens)
                    left, tokens = parse_expression(tokens)
                    stack.append((left, token, right))
                else:
                    stack.append(evaluate_term(token)[0])
            return stack

        def apply_operator(op, a, b):
            if op == 'and':
                return a and b
            elif op == 'or':
                return a or b
        expr_stack = parse_expression(tokens)
        while len(expr_stack) > 1:
            right = expr_stack.pop()
            op = expr_stack.pop()[1]
            left = expr_stack.pop()
            result = apply_operator(op, left, right)
            expr_stack.append(result)
        return expr_stack[0]
if __name__ == '__main__':
    evaluator = PredicateEvaluator([1, 2, 3, 4])
    print(evaluator.evaluate('v0 > v1'))
    print(evaluator.evaluate('v2 < v3'))
    print(evaluator.evaluate('(v0 + v1) == v2'))