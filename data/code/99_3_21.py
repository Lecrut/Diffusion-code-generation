class BooleanExpressionEvaluator:
    @staticmethod
    def evaluate(expression):
        try:
            return eval(expression)
        except Exception as e:
            return f"Error: {e}"

if __name__ == '__main__':
    expressions = [
        "(True and False) or True",
        "not (3 > 5)",
        "2 == 2 and 1 != 0",
        "4 < 7 or 8 == 9",
        "False and not True"
    ]
    for expr in expressions:
        result = BooleanExpressionEvaluator.evaluate(expr)
        print(f"Expression: {expr} -> Result: {result}")