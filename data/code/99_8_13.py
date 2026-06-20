class BooleanEvaluator:
    def check_precedence(self, expression_string):
        import operator as op
        precedence = {
            'not': 3,
            'and': 2,
            'or': 1
        }
        ops = {'not': op.not_, 'and': op.and_, 'or': op.or_}
        tokens = []
        i = 0
        while i < len(expression_string):
            if expression_string[i] == '(':
                j = i + 1
                balance = 1
                while balance != 0:
                    if expression_string[j] == '(':
                        balance += 1
                    elif expression_string[j] == ')':
                        balance -= 1
                    j += 1
                tokens.append(self.check_precedence(expression_string[i+1:j-1]))
                i = j
            else:
                j = i + 1
                while j < len(expression_string) and expression_string[j].isalnum():
                    j += 1
                tokens.append(expression_string[i:j])
                i = j

        def evaluate(tokens):
            stack_values = []
            stack_ops = []
            for token in tokens:
                if isinstance(token, str) and token.isalnum():
                    stack_values.append(bool(int(token)))
                elif isinstance(token, str) and token in precedence:
                    while (stack_ops and
                           precedence[stack_ops[-1]] >= precedence[token]):
                        right = stack_values.pop()
                        left = stack_values.pop()
                        op_func = ops[stack_ops.pop()]
                        stack_values.append(op_func(left, right))
                    stack_ops.append(token)
                elif token == '(':
                    stack_ops.append(token)
                elif token == ')':
                    while stack_ops[-1] != '(':
                        right = stack_values.pop()
                        left = stack_values.pop()
                        op_func = ops[stack_ops.pop()]
                        stack_values.append(op_func(left, right))
                    stack_ops.pop()

            while stack_ops:
                right = stack_values.pop()
                left = stack_values.pop()
                op_func = ops[stack_ops.pop()]
                stack_values.append(op_func(left, right))

            return stack_values[0]

        return evaluate(tokens)

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    expression = "not (1 and 0) or 1"
    result = evaluator.check_precedence(expression)
    print(result)