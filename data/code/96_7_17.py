import random

class ExpressionEvaluator:
    @staticmethod
    def evaluate_expression(a, b, c, d):
        return (a and b) or (c and not d)

if __name__ == '__main__':
    evaluator = ExpressionEvaluator()
    sample_values = [
        (True, True, False, False),
        (False, False, True, True),
        (True, False, True, False),
        (False, True, False, True)
    ]
    for a, b, c, d in sample_values:
        result = evaluator.evaluate_expression(a, b, c, d)
        print(f"a={a}, b={b}, c={c}, d={d} -> {result}")