class BooleanEvaluator:
    def check_precedence(self, expression_string):
        import operator as op
        precedence = {
            'not': 4,
            'and': 3,
            'or': 2
        }
        ops = {'not': op.not_, 'and': op.and_, 'or': op.or_}
        tokens = expression_string.split()
        stack = []
        output = []

        def apply_operator():
            while stack and precedence[stack[-1]] >= precedence[tokens[i]]:
                output.append(stack.pop())
            stack.append(tokens[i])

        i = 0
        while i < len(tokens):
            if tokens[i] == '(':
                stack.append(tokens[i])
            elif tokens[i] == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
            elif tokens[i] in precedence:
                apply_operator()
            else:
                output.append(tokens[i])
            i += 1

        while stack:
            output.append(stack.pop())

        def evaluate_postfix(expression):
            values = []
            for token in expression:
                if token in ops:
                    right = values.pop()
                    left = values.pop()
                    result = ops[token](left, right)
                    values.append(result)
                else:
                    values.append(token == 'True')
            return values[0]

        return evaluate_postfix(output)

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    print(evaluator.check_precedence('not True and False or True'))