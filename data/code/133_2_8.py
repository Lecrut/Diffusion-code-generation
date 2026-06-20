class BooleanEvaluator:
    TRUE = "True"
    FALSE = "False"

    @staticmethod
    def evaluate_expression(expression: str) -> bool:
        return eval(expression, {'__builtins__': None}, {BooleanEvaluator.TRUE: True, BooleanEvaluator.FALSE: False})

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    sample_expressions = [
        "True",
        "False",
        "1 == 1",
        "2 > 3"
    ]
    for expr in sample_expressions:
        result = evaluator.evaluate_expression(expr)
        print(f"Expression: {expr}, Result: {result}")