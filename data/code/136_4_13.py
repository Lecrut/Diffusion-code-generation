class BooleanExpressionEvaluator:
    TRUE = 1
    FALSE = 0

    @staticmethod
    def evaluate(expression, variables):
        expression = expression.replace("True", str(BooleanExpressionEvaluator.TRUE))
        expression = expression.replace("False", str(BooleanExpressionEvaluator.FALSE))
        for var_name, value in variables.items():
            if value:
                expression = expression.replace(var_name, str(BooleanExpressionEvaluator.TRUE))
            else:
                expression = expression.replace(var_name, str(BooleanExpressionEvaluator.FALSE))
        return eval(expression)

if __name__ == '__main__':
    evaluator = BooleanExpressionEvaluator()
    result1 = evaluator.evaluate("(A and B) or not C", {"A": True, "B": False, "C": True})
    print(f"Result: {result1}")
    result2 = evaluator.evaluate("not (X or Y)", {"X": True, "Y": False})
    print(f"Result: {result2}")
    result3 = evaluator.evaluate("A and (B or C)", {"A": True, "B": True, "C": False})
    print(f"Result: {result3}")