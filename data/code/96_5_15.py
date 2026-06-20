class ExpressionEvaluator:
    EXPRESSION_KEYS = {'A', 'B', 'C', 'D'}

    @staticmethod
    def validate_variables(variables):
        if not isinstance(variables, dict) or not all(k in variables and isinstance(v, bool) for k, v in variables.items()):
            raise ValueError("Input must be a dictionary with keys A, B, C, D and boolean values.")
        if ExpressionEvaluator.EXPRESSION_KEYS != set(variables.keys()):
            raise KeyError(f"Dictionary must contain exactly the keys {ExpressionEvaluator.EXPRESSION_KEYS}.")

    @staticmethod
    def evaluate_expression(variables):
        return (variables['A'] and variables['B']) or (variables['C'] and not variables['D'])

if __name__ == '__main__':
    sample_values = {'A': True, 'B': False, 'C': True, 'D': False}
    ExpressionEvaluator.validate_variables(sample_values)
    result = ExpressionEvaluator.evaluate_expression(sample_values)
    print(result)