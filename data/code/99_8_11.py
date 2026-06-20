class BooleanEvaluator:
    PRECEDENCE = {'not': 3, 'and': 2, 'or': 1}

    @staticmethod
    def evaluate_expression(expression):
        tokens = expression.split()
        stack_operands = []
        stack_operators = []
        for token in tokens:
            if token.isdigit() or token.lower() == 'true' or token.lower() == 'false':
                stack_operands.append(True if token.lower() == 'true' else False)
            elif token in BooleanEvaluator.PRECEDENCE:
                while stack_operators and stack_operators[-1] != '(' and (BooleanEvaluator.PRECEDENCE[token] <= BooleanEvaluator.PRECEDENCE[stack_operators[-1]]):
                    right = stack_operands.pop()
                    left = stack_operands.pop()
                    operator = stack_operators.pop()
                    result = BooleanEvaluator.perform_operation(left, right, operator)
                    stack_operands.append(result)
                stack_operators.append(token)
            elif token == '(':
                stack_operators.append(token)
            elif token == ')':
                while stack_operators[-1] != '(':
                    right = stack_operands.pop()
                    left = stack_operands.pop()
                    operator = stack_operators.pop()
                    result = BooleanEvaluator.perform_operation(left, right, operator)
                    stack_operands.append(result)
                stack_operators.pop()
        while stack_operators:
            right = stack_operands.pop()
            left = stack_operands.pop()
            operator = stack_operators.pop()
            result = BooleanEvaluator.perform_operation(left, right, operator)
            stack_operands.append(result)
        return stack_operands[0]

    @staticmethod
    def perform_operation(left, right, operator):
        if operator == 'not':
            return not left
        elif operator == 'and':
            return left and right
        elif operator == 'or':
            return left or right

    def check_precedence(self, expression_string):
        return self.evaluate_expression(expression_string)
if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    print(evaluator.check_precedence('not true'))
    print(evaluator.check_precedence('(true and false) or (true and true)'))
    print(evaluator.check_precedence('false and not false'))