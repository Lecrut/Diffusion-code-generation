import operator

class BooleanExpressionEvaluator:
    PRECEDENCE = {'(': 0, ')': 0, 'NOT': 3, 'AND': 2, 'OR': 1}

    @staticmethod
    def evaluate(expression):
        tokens = expression.split()
        stack = []
        output = []
        for token in tokens:
            if token.isalnum():
                output.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
            else:
                while stack and stack[-1] != '(' and (BooleanExpressionEvaluator.PRECEDENCE[token] <= BooleanExpressionEvaluator.PRECEDENCE[stack[-1]]):
                    output.append(stack.pop())
                stack.append(token)
        while stack:
            output.append(stack.pop())

        def apply_operator(operators, values):
            operator_ = operators.pop()
            right = values.pop()
            left = values.pop()
            if operator_ == 'NOT':
                values.append(not eval(left))
            elif operator_ in ('AND', 'OR'):
                values.append(eval(f'{left} {operator_} {right}'))
        operators = []
        values = []
        for token in output:
            if token.isalnum():
                values.append(token)
            else:
                apply_operator(operators, values)
                operators.append(token)
        while operators:
            apply_operator(operators, values)
        return values[0]
if __name__ == '__main__':
    expr1 = 'NOT True AND False OR True'
    result1 = BooleanExpressionEvaluator.evaluate(expr1)
    print(result1)
    expr2 = '(True AND False) OR (False AND NOT True)'
    result2 = BooleanExpressionEvaluator.evaluate(expr2)
    print(result2)