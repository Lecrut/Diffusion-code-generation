class BooleanEvaluator:

    def check_precedence(self, expression_string):
        import operator as op
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0, ')': 0}
        ops = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv}
        stack_ops = []
        stack_vals = []

        def apply_operator():
            while stack_ops and precedence[stack_ops[-1]] >= precedence[token]:
                b = stack_vals.pop()
                a = stack_vals.pop()
                stack_vals.append(ops[stack_ops.pop()](a, b))
        i = 0
        while i < len(expression_string):
            token = expression_string[i]
            if token.isdigit():
                j = i
                while j + 1 < len(expression_string) and expression_string[j + 1].isdigit():
                    j += 1
                stack_vals.append(int(expression_string[i:j + 1]))
                i = j + 1
            elif token in precedence:
                while stack_ops and precedence[stack_ops[-1]] >= precedence[token]:
                    apply_operator()
                if token == '(':
                    stack_ops.append(token)
                elif token == ')':
                    while stack_ops[-1] != '(':
                        apply_operator()
                    stack_ops.pop()
                else:
                    stack_ops.append(token)
                i += 1
            else:
                raise ValueError(f'Invalid character in expression: {token}')
        while stack_ops:
            apply_operator()
        return stack_vals[0]
if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    print(evaluator.check_precedence('3 + 5 * (2 - 8)'))
    print(evaluator.check_precedence('10 / 2 + 3 * 4'))