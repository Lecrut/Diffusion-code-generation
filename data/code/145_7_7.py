class BooleanExpression:
    def __init__(self, expression):
        self.expression = expression
    def evaluate(self, variables):
        if not self.expression:
            return False
        tokens = self.expression.split()
        result = []
        for token in tokens:
            if token == 'AND':
                result.append('AND')
            elif token == 'OR':
                result.append('OR')
            elif token in variables:
                result.append(variables[token])
            else:
                raise ValueError(f"Unknown token: {token}")
        return self._evaluate_recursive(result)
    def _evaluate_recursive(self, expression_list):
        if not expression_list:
            return False
        if len(expression_list) == 1:
            return expression_list[0]
        if 'AND' in expression_list:
            left = self._evaluate_recursive(expression_list[:expression_list.index('AND')])
            right = self._evaluate_recursive(expression_list[expression_list.index('AND')+1:])
            return left and right
        if 'OR' in expression_list:
            left = self._evaluate_recursive(expression_list[:expression_list.index('OR')])
            right = self._evaluate_recursive(expression_list[expression_list.index('OR')+1:])
            return left or right
        return False
def test_boolean_logic(expression_str, variables, expected):
    try:
        expr = BooleanExpression(expression_str)
        actual = expr.evaluate(variables)
        assert actual == expected, f"Expression: {expression_str}, Variables: {variables}, Expected: {expected}, Got: {actual}"
        return True
    except Exception as e:
        print(f"Error testing '{expression_str}': {e}")
        return False
if __name__ == '__main__':
    test_cases = [
        ("A AND B", {'A': True, 'B': False}, False),
        ("A OR B", {'A': True, 'B': False}, True),
        ("NOT A", {'A': False}, True),
        ("NOT (A AND B)", {'A': True, 'B': False}, True),
        ("A OR (B AND C)", {'A': True, 'B': False, 'C': True}, True),
        ("NOT (A OR B)", {'A': True, 'B': True}, False),
        ("", {}, False),
        ("A AND (B OR C)", {'A': True, 'B': True, 'C': True}, True),
        ("A OR B OR C", {'A': True, 'B': False, 'C': False}, True),
    ]
    all_passed = True
    for expression, vars_dict, expected in test_cases:
        print(f"Testing: '{expression}' with {vars_dict}: Expected={expected}")
        if not test_boolean_logic(expression, vars_dict, expected):
            all_passed = False
        print("-" * 20)
    if all_passed:
        print("All hard-coded tests passed successfully.")
    else:
        print("Some tests failed.")