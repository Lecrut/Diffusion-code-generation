class BooleanEvaluator:
    TRUE = True
    FALSE = False

    @staticmethod
    def evaluate(expression, variables):
        if not expression:
            return BooleanEvaluator.FALSE
        tokens = expression.split()
        result_stack = []
        for token in tokens:
            if token == 'AND':
                if len(result_stack) < 2:
                    raise ValueError("Malformed expression: AND requires two operands")
                right = result_stack.pop()
                left = result_stack.pop()
                result_stack.append(left and right)
            elif token == 'OR':
                if len(result_stack) < 2:
                    raise ValueError("Malformed expression: OR requires two operands")
                right = result_stack.pop()
                left = result_stack.pop()
                result_stack.append(left or right)
            elif token == 'NOT':
                if len(result_stack) < 1:
                    raise ValueError("Malformed expression: NOT requires one operand")
                operand = result_stack.pop()
                result_stack.append(not operand)
            else:
                if token in variables:
                    result_stack.append(variables[token])
                else:
                    raise KeyError(f"Unknown variable: {token}")
        return result_stack[0]

if __name__ == '__main__':
    sample_expression = "NOT (A AND B) OR C"
    sample_variables = {'A': True, 'B': False, 'C': True}
    print(BooleanEvaluator.evaluate(sample_expression, sample_variables))