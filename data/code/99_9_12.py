import operator

class BooleanExpressionEvaluator:

    def __init__(self):
        self.precedence = {'(': 0, ')': 0, 'NOT': 3, 'AND': 2, 'OR': 1}
        self.operators = {'NOT': operator.not_, 'AND': operator.and_, 'OR': operator.or_}

    def evaluate(self, expression):
        tokens = self._tokenize(expression)
        return self._eval(tokens)

    def _tokenize(self, expression):
        tokens = []
        i = 0
        while i < len(expression):
            char = expression[i]
            if char.isspace():
                i += 1
                continue
            elif char in self.precedence:
                tokens.append(char)
                i += 1
            else:
                j = i + 1
                while j < len(expression) and (not expression[j].isspace()) and (expression[j] not in self.precedence):
                    j += 1
                token = expression[i:j]
                if token.lower() == 'true':
                    tokens.append(True)
                elif token.lower() == 'false':
                    tokens.append(False)
                else:
                    raise ValueError(f'Invalid token: {token}')
                i = j
        return tokens

    def _eval(self, tokens):
        stack = []
        operators = []
        for token in tokens:
            if isinstance(token, bool):
                stack.append(token)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators[-1] != '(':
                    self._apply_operator(operators, stack)
                operators.pop()
            else:
                while operators and operators[-1] != '(' and (self.precedence[operators[-1]] >= self.precedence[token]):
                    self._apply_operator(operators, stack)
                operators.append(token)
        while operators:
            self._apply_operator(operators, stack)
        return stack[0]

    def _apply_operator(self, operators, stack):
        operator = operators.pop()
        right = stack.pop()
        left = stack.pop()
        stack.append(self.operators[operator](left, right))
if __name__ == '__main__':
    evaluator = BooleanExpressionEvaluator()
    expression = 'NOT (True AND False) OR True'
    result = evaluator.evaluate(expression)
    print(result)