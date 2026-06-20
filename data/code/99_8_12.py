import operator
OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

class BooleanEvaluator:

    def check_precedence(self, expression_string):
        tokens = self._tokenize(expression_string)
        values = []
        ops = []
        for token in tokens:
            if token.isdigit():
                values.append(int(token))
            elif token == '(':
                ops.append(token)
            elif token == ')':
                while ops and ops[-1] != '(':
                    op = ops.pop()
                    right = values.pop()
                    left = values.pop()
                    values.append(OPERATORS[op](left, right))
                ops.pop()
            else:
                while ops and ops[-1] in OPERATORS and (self._precedence(token) <= self._precedence(ops[-1])):
                    op = ops.pop()
                    right = values.pop()
                    left = values.pop()
                    values.append(OPERATORS[op](left, right))
                ops.append(token)
        while ops:
            op = ops.pop()
            right = values.pop()
            left = values.pop()
            values.append(OPERATORS[op](left, right))
        return values[0]

    def _tokenize(self, expression_string):
        tokens = []
        i = 0
        while i < len(expression_string):
            char = expression_string[i]
            if char.isdigit():
                num = int(char)
                while i + 1 < len(expression_string) and expression_string[i + 1].isdigit():
                    num = num * 10 + int(expression_string[i + 1])
                    i += 1
                tokens.append(str(num))
            elif char in OPERATORS or char in '()':
                tokens.append(char)
            i += 1
        return tokens

    def _precedence(self, operator):
        if operator in '+-':
            return 1
        if operator in '*/':
            return 2
        return 0
if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    result = evaluator.check_precedence('3 + 5 * (2 - 8)')
    print(result)