import operator

class BooleanExpressionEvaluator:
    PRECEDENCE = {'(': 0, ')': 0, 'NOT': 3, 'AND': 2, 'OR': 1}
    OPERATORS = {'NOT': operator.not_, 'AND': operator.and_, 'OR': operator.or_}

    @staticmethod
    def evaluate(expression):
        tokens = expression.replace(' ', '').split()
        stack_operands = []
        stack_operators = []
        for token in tokens:
            if token.isdigit():
                stack_operands.append(int(token))
            elif token in BooleanExpressionEvaluator.OPERATORS:
                while stack_operators and stack_operators[-1] != '(' and (BooleanExpressionEvaluator.PRECEDENCE[stack_operators[-1]] >= BooleanExpressionEvaluator.PRECEDENCE[token]):
                    right = stack_operands.pop()
                    left = stack_operands.pop()
                    operator_func = BooleanExpressionEvaluator.OPERATORS[stack_operators.pop()]
                    result = operator_func(left, right)
                    stack_operands.append(result)
                stack_operators.append(token)
            elif token == '(':
                stack_operators.append(token)
            elif token == ')':
                while stack_operators[-1] != '(':
                    right = stack_operands.pop()
                    left = stack_operands.pop()
                    operator_func = BooleanExpressionEvaluator.OPERATORS[stack_operators.pop()]
                    result = operator_func(left, right)
                    stack_operands.append(result)
                stack_operators.pop()
        while stack_operators:
            right = stack_operands.pop()
            left = stack_operands.pop()
            operator_func = BooleanExpressionEvaluator.OPERATORS[stack_operators.pop()]
            result = operator_func(left, right)
            stack_operands.append(result)
        return stack_operands[0]
if __name__ == '__main__':
    expression = 'NOT 1 AND 0 OR 1'
    result = BooleanExpressionEvaluator.evaluate(expression)
    print(result)