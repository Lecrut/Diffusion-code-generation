class ExpressionEvaluator:
    TRUE = 1
    FALSE = 0

    @staticmethod
    def evaluate_expression(a, b):
        expr1 = (a ^ b)
        expr2 = (not a) and b
        return expr1 == expr2

if __name__ == '__main__':
    sample_values = [
        (ExpressionEvaluator.TRUE, ExpressionEvaluator.FALSE),
        (ExpressionEvaluator.FALSE, ExpressionEvaluator.TRUE),
        (ExpressionEvaluator.TRUE, ExpressionEvaluator.TRUE),
        (ExpressionEvaluator.FALSE, ExpressionEvaluator.FALSE)
    ]

    for a, b in sample_values:
        result = ExpressionEvaluator.evaluate_expression(a, b)
        print(f"A={a}, B={b} -> (A XOR B) == (NOT A AND B): {result}")