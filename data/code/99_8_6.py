class BooleanEvaluator:
    def check_precedence(self, expression_string):
        import operator as op
        precedence = {
            'not': 4,
            'and': 3,
            'or': 2
        }
        ops = {'not': op.not_, 'and': op.and_, 'or': op.or_}
        
        def evaluate(tokens):
            values = []
            operators = []
            for token in tokens:
                if isinstance(token, str) and token in precedence:
                    while (operators and precedence[operators[-1]] >= precedence[token]):
                        right = values.pop()
                        left = values.pop()
                        operator = operators.pop()
                        values.append(ops[operator](left, right))
                    operators.append(token)
                else:
                    values.append(token)
            while operators:
                right = values.pop()
                left = values.pop()
                operator = operators.pop()
                values.append(ops[operator](left, right))
            return values[0]
        
        tokens = expression_string.replace('(', ' ( ').replace(')', ' ) ').split()
        return evaluate(tokens)

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    print(evaluator.check_precedence("True and False or not True"))