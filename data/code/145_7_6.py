class BooleanExpression:
    def __init__(self, expression):
        self.expression = expression
    def evaluate(self, values):
        if not isinstance(self.expression, str):
            raise TypeError("Expression must be a string.")
        tokens = self.expression.split()
        if not tokens:
            return False
        result_stack = []
        operator_stack = []
        def apply_op():
            op = operator_stack.pop()
            right = result_stack.pop()
            left = result_stack.pop()
            if op == 'AND':
                result_stack.append(left and right)
            elif op == 'OR':
                result_stack.append(left or right)
            else:
                raise ValueError(f"Unknown operator: {op}")
        for token in tokens:
            if token in ('AND', 'OR'):
                operator_stack.append(token)
            elif token in ('True', 'False'):
                result_stack.append(token == 'True')
            else:
                try:
                    value = values[token]
                    result_stack.append(value)
                except KeyError:
                    raise ValueError(f"Undefined variable: {token}")
            if (operator_stack and operator_stack[-1] in ('AND', 'OR')) and (result_stack[-1] is not None):
                apply_op()
        while operator_stack:
            apply_op()
        if len(result_stack) != 1:
            raise ValueError("Invalid expression structure or missing operands.")
        return result_stack[0]
def test_nested_logic(expression_str, variables, expected):
    try:
        expr = BooleanExpression(expression_str)
        result = expr.evaluate(variables)
        assert result == expected, f"Expression: {expression_str}, Variables: {variables}, Expected: {expected}, Got: {result}"
        return True
    except Exception as e:
        print(f"Test failed for expression '{expression_str}': {e}")
        return False
if __name__ == '__main__':
    test_cases = [
        ("True AND False", {"True": True, "False": False}, False),
        ("True OR False", {"True": True, "False": False}, True),
        ("False AND False", {"True": False, "False": False}, False),
        ("True OR True", {"True": True, "False": False}, True),
        ("True AND True AND False", {"True": True, "False": False}, False),
        ("True OR False OR True", {"True": True, "False": False}, True),
        ("False AND True", {"True": True, "False": False}, False),
        ("True OR True OR True", {"True": True, "False": False}, True),
        ("False AND False AND False", {"True": False, "False": False}, False),
        ("True OR False AND True", {"True": True, "False": False}, True),
    ]
    for expression, vars_map, expected in test_cases:
        print(f"Testing: '{expression}' with variables {vars_map}")
        test_nested_logic(expression, vars_map, expected)
        print("-" * 20)
    print("All hard-coded tests completed.")