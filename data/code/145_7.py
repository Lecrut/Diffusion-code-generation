class BooleanExpression:
    def __init__(self, expression):
        self.expression = expression
    def evaluate(self, variables):
        if not self.expression:
            return False
        tokens = self.expression.split()
        result_stack = []
        for token in tokens:
            if token == 'AND':
                if len(result_stack) < 2:
                    raise ValueError("Malformed expression: AND requires two operands")
                right = result_stack.pop()
                left = result_stack.pop()
                result_stack.append(left and right)
            elif token == 'OR':
                if len(result_stack) < 2:
                    raise ValueError("Malformed expression: OR requires two operands")
                right = result_stack.pop()
                left = result_stack.pop()
                result_stack.append(left or right)
            elif token in variables:
                result_stack.append(variables[token])
            else:
                raise ValueError(f"Unknown token: {token}")
        if len(result_stack) != 1:
            raise ValueError("Malformed expression: Expression evaluation failed")
        return result_stack[0]
class TestFramework:
    def run_tests(self, expressions_to_test, variable_set):
        results = {}
        for expr_str, expected_result in expressions_to_test.items():
            try:
                expr = BooleanExpression(expr_str)
                actual_result = expr.evaluate(variable_set)
                if actual_result == expected_result:
                    results[expr_str] = (True, actual_result)
                else:
                    results[expr_str] = (False, actual_result)
            except Exception as e:
                results[expr_str] = (False, f"Error: {e}")
        return results
if __name__ == '__main__':
    test_cases = {
        "A AND B": False,
        "A OR B": True,
        "(A AND B) OR C": True,
        "NOT A": False,
        "A AND (B OR C)": True,
        "A OR (B AND C)": True,
        "A AND A": True,
        "NOT (A OR B)": False
    }
    variable_set = {
        'A': True,
        'B': False,
        'C': True
    }
    framework = TestFramework()
    results = framework.run_tests(test_cases, variable_set)
    print("--- Test Results ---")
    for expr, (passed, actual) in results.items():
        status = "PASS" if passed else "FAIL"
        print(f"Expression: {expr}")
        print(f"  Expected: {test_cases[expr]}")
        print(f"  Actual: {actual}")
        print(f"  Status: {status}\n")