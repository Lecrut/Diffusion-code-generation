import functools
def evaluate_boolean_expression(expression, variables):
    def _evaluate_sub_expression(sub_expression, current_variables):
        if isinstance(sub_expression, bool):
            return sub_expression
        elif isinstance(sub_expression, str):
            if sub_expression in current_variables:
                return current_variables[sub_expression]
            else:
                raise ValueError(f"Undefined variable: {sub_expression}")
        elif isinstance(sub_expression, list):
            if not sub_expression:
                return False
            if len(sub_expression) == 1:
                return _evaluate_sub_expression(sub_expression[0], current_variables)
            else:
                return all(_evaluate_sub_expression(item, current_variables) for item in sub_expression)
        elif isinstance(sub_expression, dict):
            result = True
            for key, value in sub_expression.items():
                if not _evaluate_sub_expression(key, current_variables):
                    result = False
                    break
            return result
        else:
            raise TypeError(f"Unsupported expression type: {type(sub_expression)}")
    return _evaluate_sub_expression(expression, variables)
if __name__ == '__main__':
    test_cases = [
        (
            "A and (B or C)",
            {"A": True, "B": False, "C": True},
            False
        ),
        (
            "not (A and B)",
            {"A": True, "B": True},
            False
        ),
        (
            "A or B or not C",
            {"A": True, "B": False, "C": False},
            True
        ),
        (
            "not A and (B or C)",
            {"A": False, "B": True, "C": False},
            True
        ),
        (
            "A and (B or C and D)",
            {"A": True, "B": True, "C": True, "D": False},
            False
        ),
        (
            "not (A or B) and C",
            {"A": True, "B": True, "C": True},
            False
        ),
        (
            "A or B",
            {"A": True, "B": True},
            True
        ),
        (
            "A and not B",
            {"A": True, "B": False},
            True
        ),
        (
            "A and B and C",
            {"A": True, "B": True, "C": True},
            True
        ),
        (
            "not A or (B and C)",
            {"A": False, "B": True, "C": True},
            True
        ),
        (
            "A and (B or C)",
            {"A": False, "B": True, "C": False},
            False
        ),
        (
            "A and B and not C",
            {"A": True, "B": True, "C": False},
            True
        ),
        (
            "A or B or C",
            {"A": False, "B": False, "C": False},
            False
        ),
        (
            "A and (B or C)",
            {"A": True, "B": False, "C": False},
            False
        ),
        (
            "A and (B or C and D)",
            {"A": True, "B": True, "C": True, "D": False},
            False
        )
    ]
    for expression, variables, expected in test_cases:
        try:
            result = evaluate_boolean_expression(expression, variables)
            assert result == expected, f"Expression: {expression}, Variables: {variables}, Expected: {expected}, Got: {result}"
            print(f"PASS: {expression} with {variables} -> {result}")
        except Exception as e:
            print(f"FAIL: {expression} with {variables}. Error: {e}")