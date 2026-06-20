class ExpressionEvaluator:
    EXPRESSION_TEMPLATE = "(A and B) or (C and not D)"

    @staticmethod
    def evaluate(variables):
        A, B = variables[0]
        C, D = variables[2]
        return eval(ExpressionEvaluator.EXPRESSION_TEMPLATE, {'A': A, 'B': B, 'C': C, 'D': D})

if __name__ == '__main__':
    sample_values = [('A', True), ('B', False), ('C', True), ('D', False)]
    result = ExpressionEvaluator.evaluate(sample_values)
    print(result)