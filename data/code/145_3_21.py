class BooleanEvaluator:

    def evaluate_expression(self, expression):
        if not isinstance(expression, str) or not expression:
            raise ValueError('Invalid input: Expression must be a non-empty string')
        tokens = expression.split()
        result_stack = []
        operator_stack = []
        for token in tokens:
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                operand_stack.append(int(token))
            elif token in ('AND', 'OR', 'NOT'):
                if token == 'NOT':
                    if not operand_stack:
                        raise ValueError('NOT requires an operand')
                    operand = operand_stack.pop()
                    result = 0 if operand else 1
                    operand_stack.append(result)
                elif token == 'AND':
                    b = operand_stack.pop()
                    a = operand_stack.pop()
                    result = a & b
                    operand_stack.append(result)
                elif token == 'OR':
                    b = operand_stack.pop()
                    a = operand_stack.pop()
                    result = a | b
                    operand_stack.append(result)
        return operand_stack[0]
if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    expression = '1 AND 1 OR 0'
    print(evaluator.evaluate_expression(expression))