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

    random_results = []
    for _ in range(100):
        a = random.choice([True, False])
        b = random.choice([True, False])
        c = random.choice([True, False])
        d = random.choice([True, False])
        result = evaluator.evaluate_expression(a, b, c, d)
        random_results.append((a, b, c, d, result))

    for a, b, c, d, result in random_results:
        print(f"a={a}, b={b}, c={c}, d={d} -> {result}")