import random

def evaluate_expression(a, b, c, d):
    return (a and b) or (c and not d)

class ExpressionEvaluator:
    def __init__(self):
        self.sample_values = [
            (True, True, False, False),
            (False, False, True, True),
            (True, False, True, False),
            (False, True, False, True)
        ]
    
    def test_expression(self):
        for a, b, c, d in self.sample_values:
            result = evaluate_expression(a, b, c, d)
            print(f"a={a}, b={b}, c={c}, d={d} -> {result}")

if __name__ == '__main__':
    evaluator = ExpressionEvaluator()
    evaluator.test_expression()