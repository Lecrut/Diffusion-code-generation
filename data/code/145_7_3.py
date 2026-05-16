class BooleanExpression:
    def __init__(self, expression):
        self.expression = expression
    def evaluate(self, context):
        if not isinstance(self.expression, str):
            raise TypeError("Expression must be a string.")
        tokens = self.expression.split()
        if not tokens:
            return False
        result_stack = []
        for token in tokens:
            if token == 'AND':
                if len(result_stack) < 2:
                    raise ValueError("Invalid AND operation: not enough operands.")
                right = result_stack.pop()
                left = result_stack.pop()
                result_stack.append(left and right)
            elif token == 'OR':
                if len(result_stack) < 2:
                    raise ValueError("Invalid OR operation: not enough operands.")
                right = result_stack.pop()
                left = result_stack.pop()
                result_stack.append(left or right)
            elif token == 'NOT':
                if len(result_stack) < 1:
                    raise ValueError("Invalid NOT operation: not enough operands.")
                operand = result_stack.pop()
                result_stack.append(not operand)
            else:
                try:
                    value = float(token)
                    result_stack.append(bool(value))
                except ValueError:
                    raise ValueError(f"Unknown token: {token}")
        if len(result_stack) != 1:
            raise ValueError("Malformed expression resulting in incorrect stack size.")
        return result_stack[0]
class NestedBooleanTester:
    def test_expression(self, expression, context):
        try:
            result = BooleanExpression(expression).evaluate(context)
            return result
        except Exception as e:
            return f"Error: {e}"
if __name__ == '__main__':
    tester = NestedBooleanTester()
    test_cases = [
        ("True AND False", {"True": True, "False": False}),
        ("True OR False", {"True": True, "False": False}),
        ("NOT True", {"True": True}),
        ("NOT False", {"False": False}),
        ("True AND (False OR True)", {"True": True, "False": False, "True": True}),
        ("NOT (True AND False)", {"True": True, "False": False}),
        ("True OR (False AND True)", {"True": True, "False": False, "True": True}),
        ("NOT (True OR False)", {"True": True, "False": False}),
        ("True AND True AND False", {"True": True, "True": True, "False": False}),
        ("NOT True OR False", {"True": True, "False": False}),
    ]
    for expression, context in test_cases:
        result = tester.test_expression(expression, context)
        print(f"Expression: '{expression}' with context {context}: Result = {result}")
        print("-" * 20)