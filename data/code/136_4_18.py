class BooleanExpressionEvaluator:
    AND = 'and'
    OR = 'or'
    NOT = 'not'

    @staticmethod
    def evaluate(expression, variables):
        for var_name, value in variables.items():
            expression = expression.replace(var_name, str(value))
        return eval(expression)

if __name__ == '__main__':
    evaluator = BooleanExpressionEvaluator()
    expression1 = "(A and B) or not C"
    variables1 = {"A": True, "B": False, "C": True}
    result1 = evaluator.evaluate(expression1, variables1)
    print(f"Expression: {expression1}, Variables: {variables1}, Result: {result1}")

    expression2 = "not (X or Y)"
    variables2 = {"X": True, "Y": False}
    result2 = evaluator.evaluate(expression2, variables2)
    print(f"Expression: {expression2}, Variables: {variables2}, Result: {result2}")

    expression3 = "A and (B or C)"
    variables3 = {"A": True, "B": True, "C": False}
    result3 = evaluator.evaluate(expression3, variables3)
    print(f"Expression: {expression3}, Variables: {variables3}, Result: {result3}")