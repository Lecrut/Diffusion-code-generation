class BooleanEvaluator:
    def check_precedence(self, expression_string):
        import operator as op

        precedence = {
            'not': 4,
            'and': 3,
            'or': 2
        }

        ops = {'not': op.not_, 'and': op.and_, 'or': op.or_}

        def parse(tokens):
            stack = []
            while tokens:
                token = tokens.pop(0)
                if isinstance(token, str) and token in precedence:
                    while stack and precedence[token] <= precedence[stack[-1]]:
                        right = stack.pop()
                        left = stack.pop()
                        func = ops[token]
                        result = func(left, right)
                        stack.append(result)
                    stack.append(token)
                else:
                    stack.append(token)
            return stack

        def evaluate(tokens):
            while len(tokens) > 1:
                for token in precedence:
                    if token in tokens:
                        index = tokens.index(token)
                        left = evaluate(tokens[:index])
                        right = evaluate(tokens[index + 1:])
                        func = ops[token]
                        result = func(left, right)
                        return result
            return tokens[0]

        def tokenize(expression):
            expression = expression.replace(' ', '')
            tokens = []
            i = 0
            while i < len(expression):
                if expression[i] in precedence:
                    tokens.append(expression[i])
                    i += 1
                elif expression[i].isalpha():
                    j = i + 1
                    while j < len(expression) and expression[j].isalpha():
                        j += 1
                    tokens.append(expression[i:j])
                    i = j
                else:
                    raise ValueError("Invalid character in expression")
            return tokens

        tokens = tokenize(expression_string)
        parsed_tokens = parse(tokens)
        result = evaluate(parsed_tokens)
        return result

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    print(evaluator.check_precedence('not a and b or c'))
    print(evaluator.check_precedence('(a and b) or (c and d)'))
    print(evaluator.check_precedence('not (a and b) or c'))