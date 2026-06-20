class ExpressionEvaluator:
    @staticmethod
    def evaluate_expression(expression):
        return eval(expression)

if __name__ == '__main__':
    sample_expression = "2 * (3 + 4) ** 2 - 1"
    result = ExpressionEvaluator.evaluate_expression(sample_expression)
    print(f"Result of the expression '{sample_expression}': {result}")